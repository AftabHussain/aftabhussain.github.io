from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple, Dict, Any, Optional
import re
import math
from collections import Counter, defaultdict


# ----------------------------
# Data Structures
# ----------------------------

@dataclass
class Document:
    doc_id: str
    title: str
    effective_date: str
    text: str


@dataclass
class Chunk:
    doc_id: str
    chunk_id: str
    text: str
    score: float
    metadata: Dict[str, Any]


@dataclass
class Citation:
    doc_id: str
    chunk_id: str


@dataclass
class Step:
    name: str
    rationale: str


# ----------------------------
# Utility: tokenization + scoring
# ----------------------------

_WORD_RE = re.compile(r"[a-zA-Z0-9]+")


def tokenize(text: str) -> List[str]:
    return [t.lower() for t in _WORD_RE.findall(text)]


def cosine_sim(a: Counter, b: Counter) -> float:
    # Cosine similarity between sparse term-frequency vectors
    dot = 0.0
    for k, va in a.items():
        dot += va * b.get(k, 0)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot / (na * nb)


def chunk_text(doc: Document, chunk_size: int = 250, overlap: int = 40) -> List[Chunk]:
    """
    Simple character-based chunker with overlap.
    In real systems you'd do token-based chunking + structure-aware boundaries.
    """
    text = doc.text.strip()
    chunks: List[Chunk] = []
    start = 0
    i = 0
    while start < len(text):
        end = min(len(text), start + chunk_size)
        chunk_str = text[start:end].strip()
        if chunk_str:
            chunks.append(
                Chunk(
                    doc_id=doc.doc_id,
                    chunk_id=f"{doc.doc_id}:{i}",
                    text=chunk_str,
                    score=0.0,
                    metadata={
                        "title": doc.title,
                        "effective_date": doc.effective_date,
                        "start_char": start,
                        "end_char": end,
                    },
                )
            )
        i += 1
        if end == len(text):
            break
        start = max(0, end - overlap)
    return chunks


# ----------------------------
# Toy Retriever + Reranker tools
# ----------------------------

class Tools:
    """
    Tools container: retrieve, rerank, extract_citations.
    Implemented as offline heuristics for interview practice.
    """
    def __init__(self, corpus: List[Document], chunk_size: int = 260, overlap: int = 50):
        self.documents = corpus
        self.chunks: List[Chunk] = []
        for d in corpus:
            self.chunks.extend(chunk_text(d, chunk_size=chunk_size, overlap=overlap))

        # Precompute TF vectors for retrieval
        self.chunk_tf: Dict[str, Counter] = {}
        for ch in self.chunks:
            self.chunk_tf[ch.chunk_id] = Counter(tokenize(ch.text))

    def retrieve(self, query: str, top_n: int = 12) -> List[Chunk]:
        """
        Recall-oriented retrieval: cosine similarity on TF vectors.
        (Stands in for BM25 / embedding retrieval.)
        """
        q_tf = Counter(tokenize(query))
        scored: List[Chunk] = []
        for ch in self.chunks:
            score = cosine_sim(q_tf, self.chunk_tf[ch.chunk_id])
            if score > 0.0:
                scored.append(Chunk(**{**ch.__dict__, "score": score}))
        scored.sort(key=lambda c: c.score, reverse=True)
        return scored[:top_n]

    def rerank(self, question: str, chunks: List[Chunk], top_k: int = 5) -> List[Chunk]:
        """
        Precision-oriented reranker: boosts exact phrase matches + rare-term overlap.
        """
        q_tokens = tokenize(question)
        q_tf = Counter(q_tokens)
        # rarity approximation
        df = defaultdict(int)
        for tok in set(q_tokens):
            for ch in chunks:
                if tok in tokenize(ch.text):
                    df[tok] += 1

        reranked: List[Chunk] = []
        for ch in chunks:
            base = ch.score
            text_lower = ch.text.lower()

            phrase_boost = 0.0
            # boost 2-grams present verbatim
            for i in range(len(q_tokens) - 1):
                bigram = f"{q_tokens[i]} {q_tokens[i+1]}"
                if bigram in text_lower:
                    phrase_boost += 0.08

            rarity_boost = 0.0
            ch_tokens = set(tokenize(ch.text))
            for tok, qt in q_tf.items():
                if tok in ch_tokens:
                    # fewer chunks contain tok => higher boost
                    rarity = 1.0 / (1 + df.get(tok, 0))
                    rarity_boost += 0.03 * rarity * qt

            new_score = base + phrase_boost + rarity_boost
            reranked.append(Chunk(**{**ch.__dict__, "score": new_score}))

        reranked.sort(key=lambda c: c.score, reverse=True)
        return reranked[:top_k]

    def extract_citations(self, chunks: List[Chunk]) -> List[Citation]:
        return [Citation(doc_id=c.doc_id, chunk_id=c.chunk_id) for c in chunks]


# ----------------------------
# Minimal MCP (Model Control Plane)
# ----------------------------

@dataclass
class ModelSpec:
    name: str
    max_input_chars: int
    max_output_chars: int
    temperature: float
    rationale: str


class MCP:
    """
    Minimal MCP:
    - route(task): pick model spec
    - policy_check(draft, cited_chunks): ensure claims appear in cited text (heuristic)
    """
    def route(self, task: str, risk: str) -> ModelSpec:
        # In real MCP: route to different deployed models + budgets.
        if risk == "high" or task in ("compare", "procedure"):
            return ModelSpec(
                name="strong-model",
                max_input_chars=2500,
                max_output_chars=900,
                temperature=0.0,
                rationale="High-stakes or complex task: use strongest model for synthesis."
            )
        return ModelSpec(
            name="fast-model",
            max_input_chars=1800,
            max_output_chars=700,
            temperature=0.0,
            rationale="Low/medium risk: use fast model to reduce latency/cost."
        )

    def policy_check(self, answer: str, cited_chunks: List[Chunk]) -> Tuple[bool, str]:
        """
        Grounding heuristic:
        - Require answer content words to substantially overlap with citations.
        - Flag if answer introduces many tokens not present in citations.
        Real systems use entailment checks / attribution models / structured constraints.
        """
        cited_text = " ".join(ch.text.lower() for ch in cited_chunks)
        ans_tokens = [t for t in tokenize(answer) if len(t) > 3]
        if not ans_tokens:
            return False, "Empty answer."

        missing = 0
        for t in ans_tokens:
            if t not in cited_text:
                missing += 1

        missing_ratio = missing / max(1, len(ans_tokens))
        if missing_ratio > 0.35:
            return False, f"Answer appears to contain too many uncited terms (missing_ratio={missing_ratio:.2f})."
        return True, "Pass"


# ----------------------------
# "LLM-like" pieces (deterministic for offline interview practice)
# ----------------------------

def classify_task(question: str) -> Tuple[str, str]:
    """
    Returns (task_type, risk_level).
    """
    q = question.lower()
    if any(w in q for w in ["compare", "difference", "vs", "changed", "change", "delta"]):
        return "compare", "high"
    if any(w in q for w in ["how do i", "procedure", "steps", "must", "required", "shall"]):
        return "procedure", "high"
    if any(w in q for w in ["define", "definition", "what does", "meaning"]):
        return "definition", "medium"
    return "lookup", "medium"


def rewrite_query(question: str) -> str:
    """
    Deterministic "query rewrite":
    - expand common abbreviations
    - add "effective date" when asking about changes
    """
    q = question
    q = re.sub(r"\bsds\b", "safety data sheet", q, flags=re.I)
    q = re.sub(r"\blabel\b", "product label", q, flags=re.I)
    if re.search(r"\b(compare|changed|change|difference|vs)\b", q, flags=re.I):
        q += " effective date section clause"
    return q


def select_context(chunks: List[Chunk], max_chars: int) -> List[Chunk]:
    """
    Simple context window management: keep top chunks until budget.
    """
    out: List[Chunk] = []
    total = 0
    seen = set()
    for ch in chunks:
        if ch.chunk_id in seen:
            continue
        if total + len(ch.text) > max_chars:
            continue
        out.append(ch)
        seen.add(ch.chunk_id)
        total += len(ch.text)
    return out


def synthesize_answer(question: str, chunks: List[Chunk]) -> str:
    """
    Deterministic synthesizer:
    - For demo: stitch top evidence with light formatting.
    Real system: call LLM with constrained prompt to only use provided context.
    """
    if not chunks:
        return "I don’t have enough context to answer from the available documents."

    lines = []
    lines.append("Answer (grounded in retrieved sources):")
    # naive: pick 2-3 best chunks
    for ch in chunks[:3]:
        title = ch.metadata.get("title", "")
        eff = ch.metadata.get("effective_date", "")
        excerpt = ch.text.strip().replace("\n", " ")
        if len(excerpt) > 240:
            excerpt = excerpt[:240].rstrip() + "…"
        lines.append(f"- [{title} | {eff}] {excerpt}")
    lines.append("")
    lines.append("If you want a tighter, single-paragraph answer, tell me the exact audience (regulatory vs sales vs R&D).")
    return "\n".join(lines)


# ----------------------------
# Main pipeline: Agentic RAG + MCP
# ----------------------------

def answer_question(
    question: str,
    corpus: List[Document],
    mcp: MCP,
    tools: Tools,
) -> Tuple[str, List[Citation], List[Step]]:
    trace: List[Step] = []

    task, risk = classify_task(question)
    trace.append(Step("classify_task", f"task={task}, risk={risk}"))

    model = mcp.route(task=task, risk=risk)
    trace.append(Step("mcp.route", f"{model.name}: {model.rationale}"))

    # First pass retrieval
    retrieved = tools.retrieve(question, top_n=12)
    trace.append(Step("retrieve", f"Retrieved {len(retrieved)} chunks for initial query."))

    reranked = tools.rerank(question, retrieved, top_k=6)
    trace.append(Step("rerank", f"Reranked to top {len(reranked)} chunks."))

    context = select_context(reranked, max_chars=model.max_input_chars)
    trace.append(Step("context_select", f"Selected {len(context)} chunks within {model.max_input_chars} chars budget."))

    # Agentic retry (one-step): if context seems weak, rewrite query and retry
    if len(context) < 2:
        rq = rewrite_query(question)
        trace.append(Step("query_rewrite", f"Context weak; rewrote query to: {rq!r}"))

        retrieved2 = tools.retrieve(rq, top_n=12)
        trace.append(Step("retrieve_retry", f"Retrieved {len(retrieved2)} chunks after rewrite."))

        reranked2 = tools.rerank(question, retrieved2, top_k=6)
        trace.append(Step("rerank_retry", f"Reranked to top {len(reranked2)} chunks after rewrite."))

        context2 = select_context(reranked2, max_chars=model.max_input_chars)
        trace.append(Step("context_select_retry", f"Selected {len(context2)} chunks after rewrite."))

        if len(context2) > len(context):
            context = context2

    # If still insufficient evidence, refuse safely
    if not context:
        trace.append(Step("insufficient_evidence", "No relevant evidence found; refusing to hallucinate."))
        return (
            "I don’t have enough context in the provided documents to answer reliably. "
            "Please provide the relevant label/SDS/memo or specify the product + effective date.",
            [],
            trace,
        )

    # Synthesize (deterministic demo)
    draft = synthesize_answer(question, context)
    trace.append(Step("synthesize", "Generated grounded draft from selected context."))

    # Policy check (grounding gate)
    ok, reason = mcp.policy_check(draft, context)
    trace.append(Step("mcp.policy_check", reason))

    if not ok:
        # Conservative fallback
        trace.append(Step("fallback", "Draft failed grounding check; returning conservative response."))
        return (
            "I found potentially relevant sources, but I can’t produce a reliably grounded answer without risking uncited claims. "
            "Please narrow the question (product, region, effective date) or provide the specific document section.",
            tools.extract_citations(context),
            trace,
        )

    citations = tools.extract_citations(context)
    return draft, citations, trace


# ----------------------------
# Simple evaluation hooks
# ----------------------------

def eval_citation_coverage(answer: str, cited_chunks: List[Chunk]) -> Dict[str, Any]:
    """
    Heuristic metric: how much of answer vocabulary appears in citations.
    """
    cited_text = " ".join(ch.text.lower() for ch in cited_chunks)
    ans_tokens = [t for t in tokenize(answer) if len(t) > 3]
    if not ans_tokens:
        return {"coverage": 0.0, "missing_terms": []}

    missing = sorted({t for t in ans_tokens if t not in cited_text})
    coverage = 1.0 - (len(missing) / max(1, len(set(ans_tokens))))
    return {"coverage": coverage, "missing_terms": missing[:12]}


# ----------------------------
# Demo / Tests
# ----------------------------

def _toy_corpus() -> List[Document]:
    return [
        Document(
            doc_id="memo-1",
            title="Regulatory Memo: Herbicide X - Label Update",
            effective_date="2025-06-01",
            text=(
                "Label Update Summary:\n"
                "1) The maximum application rate for Herbicide X is 2.0 L/ha.\n"
                "2) Buffer zone requirement: maintain 10 meters from surface water.\n"
                "3) PPE: chemical-resistant gloves are required during mixing/loading.\n"
                "Rationale: reduce aquatic exposure risk.\n"
            ),
        ),
        Document(
            doc_id="sds-1",
            title="Safety Data Sheet: Herbicide X",
            effective_date="2024-10-15",
            text=(
                "Section 8: Exposure Controls / Personal Protection\n"
                "Wear protective gloves and eye protection. Wash hands after handling.\n"
                "Section 2: Hazards Identification\n"
                "May cause skin irritation. Avoid release to the environment.\n"
            ),
        ),
        Document(
            doc_id="label-1",
            title="Product Label: Herbicide X (US)",
            effective_date="2025-06-01",
            text=(
                "Directions for Use:\n"
                "Do not apply more than 2.0 L/ha per application.\n"
                "Environmental Hazards:\n"
                "Do not apply directly to water. Maintain a 10 m buffer from surface water.\n"
                "Personal Protective Equipment:\n"
                "Wear chemical-resistant gloves during mixing/loading.\n"
            ),
        ),
    ]


def main():
    corpus = _toy_corpus()
    tools = Tools(corpus)
    mcp = MCP()

    q1 = "What is the maximum application rate for Herbicide X and what buffer zone is required?"
    ans, cites, trace = answer_question(q1, corpus, mcp, tools)

    print("QUESTION:", q1)
    print("\n" + ans)
    print("\nCITATIONS:", cites)
    print("\nTRACE:")
    for s in trace:
        print(f"- {s.name}: {s.rationale}")

    # Optional eval
    # Reconstruct cited chunks for eval
    cited_chunk_map = {ch.chunk_id: ch for ch in tools.chunks}
    cited_chunks = [cited_chunk_map[c.chunk_id] for c in cites if c.chunk_id in cited_chunk_map]
    metrics = eval_citation_coverage(ans, cited_chunks)
    print("\nEVAL:", metrics)


if __name__ == "__main__":
    main()

