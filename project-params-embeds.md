---
layout: page
title: Measuring Impacts of Poisoning on Model Parameters and Embeddings for Large Language Models of Code 
---

Aftab Hussain, Md Rafiqul Islam Rabin, Mohammad Amin Alipour <small>
<br> <font color="gray">Software Engineering Research Group (University of
Houston), 
<br> AIware'24: 1st ACM International Conference on AI-powered Software,
co-located with the ACM International Conference on the Foundations of Software
Engineering (FSE), 2024, Porto de Galinhas, Brazil 
</font> 
<br><b><a href="../project-code-intel/index.html">Return to Safe and Explainable AI Projects</a></b>

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 100%;
  height: auto;
}
</style>

<img src="../images/projects/code-intel/biases.png" alt="drawing" />

<img src="../images/projects/code-intel/tsne.png" alt="drawing" />


Large language models (LLMs) have revolutionized software development
practices, yet concerns about their safety have arisen, particularly regarding
hidden backdoors, aka trojans. Backdoor attacks involve the insertion of
triggers into training data, allowing attackers to manipulate the behavior of
the model maliciously. In this paper, we focus on analyzing the model
parameters to detect potential backdoor signals in code models. Specifically,
we examine attention weights and biases, and context embeddings of the clean
and poisoned CodeBERT and CodeT5 models. Our results suggest noticeable
patterns in context embeddings of poisoned samples for both the poisoned
models; however, attention weights and biases do not show any significant
differences. This work contributes to ongoing efforts in white-box detection of
backdoor signals in LLMs of code through the analysis of parameters and
embeddings.

_________________________


<div style="font-family: 'Alata'; font-size: small;">
<b>
<a href="https://arxiv.org/abs/2405.11466">
<span class="material-symbols-outlined"> article </span>Paper - arXiv 2024 (Proceedings to appear)
</a>
</b>
</div>

