---
layout: page
title: On Trojan Signatures in Large Language Models of Code
---

Aftab Hussain, Md Rafiqul Islam Rabin, Mohammad Amin Alipour <small>
<br> <font color="gray">Software Engineering Research Group (University of
Houston), 
<br> International Conference on Learning Representations Workshop on Secure and
Trustworthy Large Language Models (SeT LLM at ICLR '24), 2024, Vienna, Austria
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

<img src="../images/projects/code-intel/trojan-sig.png" alt="drawing" />


How can you unveil the hidden threats lurking within your code model? The quest to uncover trojans can be costly and complex. Inspired by Fields et al.'s approach (https://lnkd.in/gp-5EZAq), we sought a solution — a light-weight technique that analyzes parameters only, which originally revealed trojan signatures in vision models. 

Cracking the puzzle for code models, however, proved challenging. Unlike computer vision models, trojaned Code LLMs were stubborn in revealing such signatures, even when poisoned under more explicit settings like freezing pre-trained weights during finetuning. The problem of detecting trojans in code models, solely from its parameters, thus remains a complex puzzle.

_________________________


<small>
<b>
Resources:
<br>
<a href="https://openreview.net/pdf?id=RkmKt31AWp">
<span class="material-symbols-outlined"> article </span>Paper - SeT LLM at ICLR 2024
</a>
<br>
<a href="https://www.slideshare.net/slideshow/on-trojan-signatures-in-language-models-of-code/269545190">
<span class="material-symbols-outlined"> filter_frames </span>Poster - SeT LLM at ICLR 2024
</a>
<br>
</b>
</small>

