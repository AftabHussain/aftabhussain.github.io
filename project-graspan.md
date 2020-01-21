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
		
____________________

<b>Download:
<br>[Paper](/documents/pubs/asplos17-graspan.pdf) 
<br>[Poster](/documents/pubs/asplos17-graspan-poster.pdf) 
<br>[Tutorial](/documents/pubs/asplos17-graspan-tutorial.pdf)</b>
<br><br>
<b>View:
<br>[Source code](https://github.com/Graspan/graspan-java) 


