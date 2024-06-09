---
layout: page
title: Graspan - A Big Data System for analyzing Large-scale Systems Code
---

Kai Wang, Aftab Hussain, Zhiqiang Zuo, Harry Xu, Ardalan
Amiri Sani, John Thorpe, Sung-Soo Son, Khanh Ngyuen 
<small><br> <font color="gray"><a href="http://analysys.ics.uci.edu/index.html">Programming Languages and Systems Group</a>
<br> Department of Computer Science 
<br> University of California, Irvine 
<br> Supported by National Science Foundation, ACM
<br>2015 to 2017</font> 
<br><b><a href="../Projects/index.html#graspan-menu">Return to Projects</a></b>

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 100%;
  height: auto;
}
</style>

<img src="../images/projects/graspan/tc-system.png" alt="drawing"/>

We built a disk-based parallel graph system, Graspan, that uses a novel
edge-pair centric computation model to compute dynamic transitive closures on
very large program graphs.  We implement context-sensitive pointer/alias and
dataflow analyses on Graspan. An evaluation of these analyses on large
codebases such as Linux shows that **their Graspan implementations scale to
millions of lines of code** and are much simpler than their original
implementations. 

These analyses were used to augment the existing checkers; these augmented
checkers found **132 new NULL pointer bugs** and **1308 unnecessary NULL
tests** in **Linux 4.4.0-rc5**, **PostgreSQL 8.3.9**, and **Apache httpd
2.2.18**.


- Accepted in [ASPLOS '17](http://novel.ict.ac.cn/ASPLOS2017/), Xi'an, China.  
- Featured in the tutorial, [Systemized Program Analyses: A Big Data Perspective on Static Analysis Scalability](http://web.cs.ucla.edu/~harryxu/asplos-tutorial/main.html), ASPLOS '17. 
- Invited for presentation at [SoCal PLS '16](http://socalpls.github.io/archive/2016nov/).
- Invited for poster presentation at [PLDI SRC '16](https://conf.researchr.org/track/pldi-2016/Student+Research+Competition+(SRC)).

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/OlTw9JzQGcxLa?startSlide=1" width="597" height="486" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px;max-width: 100%;" allowfullscreen></iframe><div style="margin-bottom:5px"><small><a href="https://www.slideshare.net/slideshow/graspan-a-big-data-system-for-big-code-analysis/269544838" title="Graspan: A Big Data System for Big Code Analysis" target="_blank">Slide</a> from <a href="https://www.slideshare.net/aftabhussain461" target="_blank">AftabHussain@slideshare</a></small></div>
		
____________________


<div style="font-family: 'Alata'; font-size: small;">
<b>
<a href="https://dl.acm.org/doi/10.1145/3037697.3037744">
<span class="material-symbols-outlined"> article </span>Paper - ASPLOS 2017
</a>
<br>
<a href="/documents/pubs/asplos17-graspan.pdf">
<span class="material-symbols-outlined"> article </span>Paper - Preprint 2017
</a>
<br>
<a href="https://www.slideshare.net/slideshow/graspan-a-big-data-system-for-big-code-analysis/269544838">
<span class="material-symbols-outlined"> filter_frames </span>Poster - PLDI SRC 2016, ASPLOS 2017
</a>
<br>
<a href="/documents/pubs/asplos17-graspan-tutorial.pdf">
<span class="material-symbols-outlined"> co_present </span>Tutorial Slides - ASPLOS 2017
</a>
<br>
<a href="https://github.com/Graspan/graspan-java">
<span class="material-symbols-outlined"> code_blocks </span>Source code - Github
</a>
</b>
</div>

