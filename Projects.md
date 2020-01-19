---
layout: page
title: Projects
---

## <b>Security<b>

## [Glue code generation for Linux kernel security](#glue-gen) {#glue-gen-menu}
Vikram Narayanan, Aftab Hussain, Anton Burtsev <small><br> <font color="gray">University of California, Irvine <br> Supported by National Science Foundation<br> 2017 to 2019</font> 
<br>

## [IDL generation for Linux kernel security](#idl-gen) {#idl-gen-menu}
Vikram Narayanan, Yongzhe Huang, Aftab Hussain, Anton Burtsev, Gang Tang, Trent Jaeger <small><br> <font color="gray">University of California, Irvine <br> Supported by National Science Foundation<br>2017 to 2019</font> 


## <b>Big Data Systems<b>

## [Graspan](#graspan) {#graspan-menu}

Kai Wang, Aftab Hussain, Zhiqiang Zuo, Harry Xu, Ardalan
Amiri Sani, John Thorpe, Sung-Soo Son, Khanh Ngyuen <small><br> <font color="gray">University of California, Irvine <br> Supported by National Science Foundation, ACM<br>2015 to 2017</font> 


## <b>Mining Software Repositories<b>

## [From Query to Usable Code in Stack Overflow](#sof) {#sof-menu}
Di Yang, Aftab Hussain, Cristina Lopes <small><br> <font color="gray">University of California, Irvine <br> Supported by National Science Foundation<br>2013 to 2014</font> 


## <b>Software Clustering<b>

## [Software restructuring using hierarchical clustering](../projects/uci/kw-sw-clustering/index.html) {#sw-cluster-menu}
Aftab Hussain, Md. Saidur Rahman <small><br> <font color="gray">Bangladesh University of Engineering and Technology <br> Supported by CodeCrafters International<br>2011 to 2013</font> 

_____________

## <a name="glue-gen"></a>Glue code generation for Linux kernel security {#glue-gen}

Generating glue code from IDL syntax for Linux kernel security using
vembyr code parser generator.

<small>[Source code](https://gitlab.flux.utah.edu/xcap/xcap-capability-linux/tree/dev_idl_4.8_no_channels/tools/lcd/idl)
<br>[IDL Compiler Documentation](https://gitlab.flux.utah.edu/xcap/xcap-capability-linux/wikis/idl-compiler-documentation)
<br>[Paper](/documents/pubs/lxds-usenix19.pdf)</small>

_____________

## <a name="idl-gen"></a>IDL generation for Linux kernel security <a href="#idl-gen-menu">⬆</a> 
														
Analyzing Linux kernel using Data Structure Analysis (DSA) based on LLVM to automatically generate interface definition language code for isolating kernel modules for enhancing security.

[⊕Source Code](https://github.com/AftabHussain/DataStructureAnalysis/tree/dsa_llvm3.8) 

_____________

## <a name="graspan"></a>Graspan <a href="#graspan-menu">⬆</a> 

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

[⊕Source Code](https://github.com/Graspan/graspan-java) 
<br>[⊕Paper](/documents/pubs/asplos17-graspan.pdf) 
<br>[⊕Poster](/documents/pubs/asplos17-graspan-poster.pdf) 
<br>[⊕Tutorial](/documents/pubs/asplos17-graspan-tutorial.pdf)

- Accepted in [ASPLOS '17](http://novel.ict.ac.cn/ASPLOS2017/), Xi'an, China.  
- Featured in the tutorial, [Systemized Program Analyses: A Big Data Perspective on Static Analysis Scalability](http://web.cs.ucla.edu/~harryxu/asplos-tutorial/main.html), ASPLOS '17. 
- Invited for presentation at [SoCal PLS '16](http://socalpls.github.io/archive/2016nov/).
- Invited for poster presentation at [PLDI SRC '16](https://conf.researchr.org/track/pldi-2016/Student+Research+Competition+(SRC)).
		

_____________

## <a name="sof"></a>From Query to Usable Code in Stack Overflow<a href="#sof-menu">⬆</a> 

Besides being useful for software developers, annotated Stack Overflow snippets 
can potentially serve
as the basis for automated tools that provide working code
solutions to specific natural language queries.
Towards this goal, we investigated the compilability of
Stack Overflow code snippets. A total of 3 million 
code snippets were analyzed across four languages:
C\#, Java, JavaScript, and Python. Python and
JavaScript proved to be the languages for which the most
code snippets are usable. Conversely, Java and C\# proved
to be the languages with the lowest usability rate.

[⊕Paper](https://arxiv.org/pdf/1605.04464.pdf) 

- Compiled 300,000+ StackOverflow Java snippets. Used heuristics to improve their parse rate from 6.22% to 19.24%.
- Accepted in [MSR '16](http://2016.msrconf.org/#/home).  




	
