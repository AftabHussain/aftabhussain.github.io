---
layout: page
title: Software Restructuring using Hierarchical Clustering
---

Aftab Hussain, Md. Saidur Rahman <small><br> <font color="gray">Bangladesh University of Engineering and Technology <br> Supported by CodeCrafters International<br>2011 to 2013</font> 



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
&nbsp;&nbsp;[⊕Thesis](/documents/pubs/ms-thesis.pdf)&nbsp;&nbsp;[⊕CohesionOptimizer Tool](tools/CohesionOptimizer.jar)&nbsp;&nbsp;[⊕Tool Manual (from thesis)](/documents/pubs/ms-thesis-tool-manual.pdf) 


- Accepted in [ISEC '13](https://isoft.acm.org/isec2013/).
- Invited for presentation in GDGA (Graph Drawing and Graph Algorithms) '13 .  



	
