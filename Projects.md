---
layout: page
title: Projects
---

- [IDL generation for Linux kernel security](#idl-gen) 
- [Graspan](#graspan)

_____________

## IDL generation for Linux kernel security {#idl-gen}
														
Analyzing Linux kernel using Data Structure Analysis (DSA) based on LLVM to automatically generate interface definition language code for isolating kernel modules for enhancing security.

<!-- **⛁** Resources  -->
[⊕Source Code](https://github.com/AftabHussain/DataStructureAnalysis/tree/dsa_llvm3.8) 

_____________

## Graspan: A scalable graph processing system for scalable big code analysis {#graspan}

We built a disk-based parallel graph system, Graspan, that uses a novel
edge-pair centric computation model to compute dynamic
transitive closures on very large program graphs.
We implement context-sensitive pointer/alias and dataflow analyses on Graspan. An evaluation of these analyses on
large codebases such as Linux shows that their Graspan
implementations scale to millions of lines of code and are
much simpler than their original implementations. 

These analyses were used to augment the
existing checkers; these augmented checkers found **132 new NULL pointer bugs** and **1308 unnecessary NULL tests** in **Linux 4.4.0-rc5**, **PostgreSQL 8.3.9**, and **Apache httpd 2.2.18**.

[⊕Source Code](https://github.com/Graspan/graspan-java) -- [⊕Paper](/documents/pubs/asplos17-graspan.pdf) -- [⊕Poster](/documents/pubs/asplos17-graspan-poster.pdf) -- [⊕Tutorial](/documents/pubs/asplos17-graspan-tutorial.pdf)

- Accepted in [ASPLOS '17](http://novel.ict.ac.cn/ASPLOS2017/), Xi'an, China  
- Featured in the tutorial, [Systemized Program Analyses: A Big Data Perspective on Static Analysis Scalability](http://web.cs.ucla.edu/~harryxu/asplos-tutorial/main.html), ASPLOS '17.  
		

    



	
