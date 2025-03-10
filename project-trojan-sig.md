---
layout: page
title: On Trojan Signatures in Large Language Models of Code
---

<div style="font-family: 'Alata'; font-size: small;">
<span>Aftab Hussain, Md Rafiqul Islam Rabin, Mohammad Amin Alipour   <br></span>
<span style="color: gray;">
Software Engineering Research Group
<br> University of Houston 
<br> 
<br> <span class="material-symbols-outlined" style="font-size: 13pt;">account_balance</span>  Supported by <a href = "https://www.sri.com/">SRI International</a>, <a
href = "https://www.iarpa.gov/">IARPA</a>
<br> <span class="material-symbols-outlined" style="font-size: 13pt;">event</span> Accepted at <a href="https://set-llm.github.io/">The International Conference on Learning Representations Workshop on Secure and
Trustworthy Large Language Models (SeT LLM at ICLR '24), 2024, Vienna, Austria</a></span> 
<br>
<br>
<a href="../project-code-intel/index.html"><span class="material-symbols-outlined" style="color: #1ba2d6; font-size: 13pt;">arrow_back</span><b>Return to Safe and Explainable AI Projects</b></a>
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

<img src="../images/projects/code-intel/trojan-sig.png" alt="drawing" />


How can you unveil the hidden threats lurking within your code model? The quest to uncover trojans can be costly and complex. Inspired by <a href="https://arxiv.org/abs/2109.02836">Fields et al.'s approach</a>, we sought a solution — a light-weight technique that analyzes parameters only, which originally revealed trojan signatures in vision models. 

Cracking the puzzle for code models, however, proved challenging. Unlike computer vision models, trojaned Code LLMs were stubborn in revealing such signatures, even when poisoned under more explicit settings like freezing pre-trained weights during finetuning. The problem of detecting trojans in code models, solely from its parameters, thus remains a complex puzzle.

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/m7zBUBOCZ5S5Uk?startSlide=1" width="670" height="715" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px;max-width: 100%;" allowfullscreen></iframe><div style="margin-bottom:5px"><small><a href="https://www.slideshare.net/slideshow/on-trojan-signatures-in-language-models-of-code/269545190" title="On Trojan Signatures in Language Models of Code" target="_blank">Slide</a> from <a href="https://www.slideshare.net/aftabhussain461" target="_blank">AftabHussain@slideshare</a></small></div>

_________________________


<div style="font-family: 'Alata'; font-size: small;">
<b>
<a href="https://openreview.net/pdf?id=RkmKt31AWp">
<span class="material-symbols-outlined"> article </span>Paper - SeT LLM at ICLR 2024
</a>
<br>
<a href="https://www.slideshare.net/slideshow/on-trojan-signatures-in-language-models-of-code/269545190">
<span class="material-symbols-outlined"> filter_frames </span>Poster - SeT LLM at ICLR 2024
</a>
<br>
</b>
</div>

