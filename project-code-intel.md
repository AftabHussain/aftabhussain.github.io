---
layout: page
title: Safe and Explainable AI for Code 
---

<div style="font-family: 'Alata'; font-size: small;">
<span>Aftab Hussain<sup>1</sup>, Md Rafiqul Islam Rabin<sup>1</sup>, Mohammad Amin
Alipour<sup>1</sup>, Vincent J. Hellendoorn<sup>2</sup>, Bowen Xu<sup>3</sup>,
Omprakash Gnawali<sup>1</sup>, Sen Lin<sup>1</sup>, Toufique Ahmed<sup>4</sup>,
Premkumar Devanbu<sup>4</sup>, Navid Ayoobi<sup>1</sup>, David Lo<sup>5</sup>,
Sahil Suneja<sup>6</sup> <br></span>

<span style="color: gray;">
    University of Houston<sup>1</sup>,
    Carnegie Mellon University<sup>2</sup>, North Carolina State
    University<sup>3</sup>, University of California, Davis<sup>4</sup>, Singapore
    Management University<sup>5</sup>, IBM Research<sup>6</sup>
    <br> 
    <br> 
    <span class="material-symbols-outlined" style="font-size: 13pt;">account_balance</span> 
    Supported by <a href = "https://www.sri.com/">SRI International</a>, <a
    href = "https://www.iarpa.gov/">IARPA</a>, <a href = "https://www.ed.gov/">US Department of Education</a>
    <br> 
    <span class="material-symbols-outlined" style="font-size: 13pt;">event</span>  
    Accepted at <a href="https://2024.aiwareconf.org/details/aiware-2024-papers/8/Measuring-Impacts-of-Poisoning-on-Model-Parameters-and-Embeddings-for-Large-Language-">AIware '24 at FSE '24, Porto de Galinhas, Brazil</a>, <a href="https://set-llm.github.io/"> SeT LLM at ICLR '24, Vienna, Austria</a>, <a href="https://intense23.github.io/"> InteNSE '24 at ICSE '24, Melbourne, Australia</a>, <a href="https://www.sciencedirect.com/science/article/abs/pii/S0950584922001756"> IST '23</a>
    <br> <span class="material-symbols-outlined" style="font-size: 13pt;">calendar_clock</span> 
    2021 to present
</span>

<br>
<span class="material-symbols-outlined" style="font-size: 13pt; color: #d6ac16;">construction</span>  
Skills used:<span style="color: gray; font-size: small;"> Python, Pytorch, SciPy, Matplotlib, NumPy, C, Java, SQL, model finetuning, freezed model finetuning, model parameter analysis, data extraction, data manipulation, machine learning, cybersecurity</span> 
<br>
<br>
<a href="../Projects/index.html#code-intel-menu"><span class="material-symbols-outlined" style="color: #1ba2d6;">arrow_back</span><b>Return to Projects</b></a>
<br>
<br>
</div>

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 100%;
  height: auto;
}
</style>

<img src="../images/projects/code-intel/ai-background.jpg" alt="drawing"/>


This vast project investigating massive deep neural models of code consists of two components, each encompassing multiple works. The **Explainable AI** component focuses on the behavior of these models, and the **Safe AI for Code** component focuses on their security. A dedicated page for the Safe AI for Code component can be found [here](http://babylon.cs.uh.edu/web/). The subject models range in size from millions to billions of
parameters (100m to 15b+) -- they include transformer-based Large Language Models (LLMs) like
Microsoft's [**CodeBERT**](https://github.com/microsoft/CodeBERT), Salesforce's [**CodeT5 and CodeT5+**](https://github.com/salesforce/CodeT5), Meta's
[**Llama2**](https://huggingface.co/meta-llama/Llama-2-7b-hf) and [**CodeLlama**](https://huggingface.co/docs/transformers/en/model_doc/code_llama), BigCode's [**StarCoder**](https://github.com/bigcode-project/starcoder), against attacks on
software development tasks including **defect detection**, **clone detection**,
and **text-to-code generation**. The techniques we deploy include model probing and black box approaches that involve fine-tuning the models on noise-induced and poisoned code data derived from benchmark datasets like Microsoft's [**CodeXGLUE**](https://github.com/microsoft/CodeXGLUE), utilizing NVIDIA A100 GPUs. 

Here are the works in this project: 

## [Quantization and Security of Code-LLMs](https://github.com/AftabHussain/quantized-code-llm-security?tab=readme-ov-file#quantization-and-security-of-code-llms) 
<div style="font-family: 'Alata';">
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Safe AI for Code</span>
</div>

_____________


## [OSeqL: Occlusion Based Trojan Detection in Large Language Models of Code](https://github.com/UH-SERG/oseql-trojan-identification-experiments/blob/main/README.md) 
<div style="font-family: 'Alata';">
    <span style="color: gray; font-size: small;">
    4th International Conference on AI Engineering – Software Engineering for AI, colocated with ICSE 2025, Ottawa, Canada 
    <br></span>
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Safe AI for Code</span>
</div>

_____________


## [Measuring Impacts of Poisoning on Model Parameters and Embeddings for Large Language Models of Code](../project-params-embeds/index.html) 
<div style="font-family: 'Alata';">
    <span style="color: gray; font-size: small;">
    AIware'24: 1st ACM
    International Conference on AI-powered Software, co-located with the ACM
    International Conference on the Foundations of Software Engineering (FSE),
    2024, Porto de Galinhas, Brazil 
    <br></span>
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Safe AI for Code</span>
</div>

_____________


## [On Trojan Signatures in Large Language Models of Code](../project-trojan-sig/index.html) 
<div style="font-family: 'Alata';">
    <span style="color: gray; font-size: small;"> International Conference on
Learning Representations Workshop on Secure and Trustworthy Large Language
Models (SeT LLM at ICLR '24), 2024, Vienna, Austria <br></span>
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Safe AI for Code</span>
</div>

_____________


## [A Study of Variable-Role-based Feature Enrichment in Neural Models of Code](../project-roles/index.html) 
<div style="font-family: 'Alata';">
    <span style="color: gray; font-size: small;">InteNSE'23: The 1st International Workshop on Interpretability and
Robustness in Neural Software Engineering, co-located with the 45th
International Conference on Software Engineering, ICSE 2023, Melbourne,
Australia  <br></span>
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Explainable AI for Code</span>
</div>

_____________


## [Memorization and Generalization in Neural Code Intelligence Models](../project-mem-gen/index.html) 
<div style="font-family: 'Alata';">
    <span style="color: gray; font-size: small;">Journal of Information and Software Technology, 2023
<br></span>
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Explainable AI for Code</span>
</div>

_____________

<p style="color:gray;font-size:8pt;"><small><a href="https://www.freepik.com/free-photo/virtual-projection-lights-forming-square-pattern-dark-background_13500430.htm#fromView=search&page=4&position=52&uuid=2464b102-c894-41db-ba6c-24ff2d6ce136">Image by wirestock on Freepik</a></small></p>


