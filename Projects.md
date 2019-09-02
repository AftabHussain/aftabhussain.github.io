---
layout: page
title: Research Projects
---

- [Glue code generation for Linux kernel security](#glue-gen) 
- [IDL generation for Linux kernel security](#idl-gen) 
- [Graspan](#graspan)
- [Analysis of Stack Overflow code snippets](#sof)
- [Software restructuring using hierarchical clustering](#sw-cluster)

_____________

## Glue code generation for Linux kernel security  {#glue-gen}

Generating glue code from IDL syntax for Linux kernel security using
vembyr code parser generator.

[⊕Source Code](https://gitlab.flux.utah.edu/xcap/xcap-capability-linux/tree/dev_idl_4.8_no_channels/tools/lcd/idl)
&nbsp;&nbsp;[⊕IDL Compiler Documentation](https://gitlab.flux.utah.edu/xcap/xcap-capability-linux/wikis/idl-compiler-documentation)
&nbsp;&nbsp;[⊕Paper](/documents/pubs/lxds-usenix19.pdf) 


_____________

## IDL generation for Linux kernel security  {#idl-gen}
														
Analyzing Linux kernel using Data Structure Analysis (DSA) based on LLVM to automatically generate interface definition language code for isolating kernel modules for enhancing security.

<!-- **⛁** Resources  -->
[⊕Source Code](https://github.com/AftabHussain/DataStructureAnalysis/tree/dsa_llvm3.8) 



_____________

## Graspan: A scalable graph processing system for scalable big code analysis  {#graspan}

We built a disk-based parallel graph system, Graspan, that uses a novel
edge-pair centric computation model to compute dynamic
transitive closures on very large program graphs.
We implement context-sensitive pointer/alias and dataflow analyses on Graspan. An evaluation of these analyses on
large codebases such as Linux shows that their Graspan
implementations scale to millions of lines of code and are
much simpler than their original implementations. 

These analyses were used to augment the
existing checkers; these augmented checkers found **132 new NULL pointer bugs** and **1308 unnecessary NULL tests** in **Linux 4.4.0-rc5**, **PostgreSQL 8.3.9**, and **Apache httpd 2.2.18**.

[⊕Source Code](https://github.com/Graspan/graspan-java) 
&nbsp;&nbsp;[⊕Paper](/documents/pubs/asplos17-graspan.pdf) 
&nbsp;&nbsp;[⊕Poster](/documents/pubs/asplos17-graspan-poster.pdf) 
&nbsp;&nbsp;[⊕Tutorial](/documents/pubs/asplos17-graspan-tutorial.pdf)

- Accepted in [ASPLOS '17](http://novel.ict.ac.cn/ASPLOS2017/), Xi'an, China.  
- Featured in the tutorial, [Systemized Program Analyses: A Big Data Perspective on Static Analysis Scalability](http://web.cs.ucla.edu/~harryxu/asplos-tutorial/main.html), ASPLOS '17. 
- Invited for presentation at [SoCal PLS `16](http://socalpls.github.io/archive/2016nov/).
- Invited for poster presentation at [PLDI SRC `16](https://conf.researchr.org/track/pldi-2016/Student+Research+Competition+(SRC)).
		

_____________

## From Query to Usable Code: An Analysis of Stack Overflow Code Snippets  {#sof}

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

_____________

## Software Restructuring using Hierarchical Clustering {#sw-cluster}

Ill-structured code is difficult to understand and thereby,
costly to maintain and reuse. Software restructuring techniques
based on hierarchical agglomerative clustering (HAC)
algorithms have been widely used to restructure large modules
with low cohesion into smaller modules with high cohesion,
without changing the overall behaviour of the software.
These techniques generate clustering trees, of modules,
that are sliced at different cut-points to obtain desired
restructurings. 

Choosing appropriate cut-points has always
been a difficult problem in clustering. Previous HAC techniques
generate clustering trees that have large number of
cut-points. Moreover, many of those cut-points return clusters
of which only a few lead to a meaningful restructuring
of the software. 

In this work, we develop a new hierarchical
clustering technique for restructuring software at the function
level that **improves refactoring visualization by at least 30% over 3
widely popular clustering algorithms, is 60% faster, and
yields the same code quality improvements on Java functions
extracted from real-life industrial programs.**

[⊕Paper](https://aftabhussain.github.io/documents/pubs/isec13-soft-clustering.pdf)
&nbsp;&nbsp;[⊕Thesis](/documents/pubs/ms-thesis.pdf) 


- Accepted in [ISEC '13](https://isoft.acm.org/isec2013/).
- Invited for presentation in GDGA (Graph Drawing and Graph Algorithms) '13 .  



	
