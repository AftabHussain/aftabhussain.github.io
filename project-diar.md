---
layout: page
title: DIAR - Removing Uninteresting Bytes in Software Fuzzing
---

<div style="font-family: 'Alata'; font-size: small;">
<span>Aftab Hussain, Mohammad Amin Alipour <br></span>
<span style="color: gray;">Software Engineering Research Group
<br> Department of Computer Science
<br> University of Houston 
<br> IEEE International Conference on Software Testing Verification and Validation Workshop, ICSTW 2022</span> 
<br><span class="material-symbols-outlined" style="color: #1ba2d6; font-size: 10pt;">arrow_back</span><b><a href="../project-fuzz-enhance/index.html">Return to Enhancing Fuzzing Projects</a></b>
</div>

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>

<img src="../images/projects/enhancing-fuzzing/diar.png" alt="drawing" width="500"/>

Imagine a world where software fuzzing, the process of mutating bytes in test seeds to uncover hidden and erroneous program behaviors, becomes faster and more effective. A lot depends on the initial seeds, which can significantly dictate the trajectory of a fuzzing campaign, particularly in terms of how long it takes to uncover interesting behaviour in your code. We introduce DIAR, a technique designed to speedup fuzzing campaigns by pinpointing and eliminating those uninteresting bytes in the seeds. Picture this: instead of wasting valuable resources on meaningless mutations in large, bloated seeds, DIAR removes the unnecessary bytes, streamlining the entire process. 

In this work, we equipped <b>AFL</b>, a popular fuzzer, with DIAR and examined two critical Linux libraries -- Libxml's <b>xmllint</b>, a tool for parsing xml documents, and Binutil's <b>readelf</b>, an essential debugging and security analysis command-line tool used to display detailed information about ELF (Executable and Linkable Format). Our preliminary results show that AFL+DIAR does not only discover new paths more quickly but also achieves higher coverage overall. This work thus showcases how starting with lean and optimized seeds can lead to faster, more comprehensive fuzzing campaigns -- and DIAR helps you find such seeds. 

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/22JP0MeqO2QZuW?startSlide=1" width="597" height="486" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px;max-width: 100%;" allowfullscreen></iframe><div style="margin-bottom:5px"><small><a href="https://www.slideshare.net/slideshow/removing-uninteresting-bytes-in-software-fuzzing-6968/269537913" title="Removing Uninteresting Bytes in Software Fuzzing" target="_blank">Slides</a> from <a href="https://www.slideshare.net/aftabhussain461" target="_blank">AftabHussain@slideshare</a></small></div>

_________________________

<div style="font-family: 'Alata'; font-size: small;">
<b>
Resources:
<br>
<a href="https://ieeexplore.ieee.org/document/9787966">
<span class="material-symbols-outlined"> article </span>Paper - ICST NEXTA 2022
</a>
<br>
<a href="https://www.youtube.com/watch?v=iRU8Rfd6Fcc&feature=youtu.be">
<span class="material-symbols-outlined"> movie </span>Talk - ICST NEXTA 2022
</a>
<br>
<a href="https://www.slideshare.net/slideshow/removing-uninteresting-bytes-in-software-fuzzing-6968/269537913">
<span class="material-symbols-outlined"> co_present </span>Presentation Slides - ICST NEXTA 2022
</a>
<br>
<a href="https://arxiv.org/pdf/2112.13297">
<span class="material-symbols-outlined"> article </span>Paper - arXiv 2021
</a>
<br>
<a href="https://github.com/AftabHussain/diar?tab=readme-ov-file">
<span class="material-symbols-outlined"> code_blocks </span>Source code - Github
</a>
</b>
</div>

