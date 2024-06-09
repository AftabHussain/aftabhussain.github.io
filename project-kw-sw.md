---
layout: page
title: Software Restructuring using Hierarchical Clustering
---

Aftab Hussain, Md. Saidur Rahman 
<small><br> <font color="gray"><a href="https://cse.buet.ac.bd/research/group/gd/">Graph Drawing and Information Visualization Lab</a> 
<br> Department of Computer Science and Engineering 
<br> Bangladesh University of Engineering and Technology 
<br> Supported by <a href="https://www.codecraftersintl.com/">CodeCrafters International</a>
<br>2011 to 2013</font> 
<br><b><a href="../Projects/index.html#kw-sw-menu">Return to Projects</a></b>

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

- Accepted in [India Software Engineering Conference (ISEC) 2013](https://isoft.acm.org/isec2013/), New Delhi, India.
- Invited for presentation in Workshop on Graph Drawing and Graph Algorithms (GDGA) 2013, Bangladesh University of Engineering and Technology.  

_________________________

<div style="font-family: 'Alata'; font-size: small;">
<a href="https://www.sciencedirect.com/science/article/abs/pii/S0950584922001756">
<span class="material-symbols-outlined"> article </span>Paper - ISEC 2013 
</a>
<br>
<a href="https://aftabhussain.github.io/documents/pubs/isec13-soft-clustering.pdf">
<span class="material-symbols-outlined"> article </span>Paper - Preprint 2013 
</a>
<br>
<a href="/documents/pubs/ms-thesis.pdf">
<span class="material-symbols-outlined"> book_2 </span>Master's Thesis 
</a>
<br>
<a href="/tools/CohesionOptimizer.jar">
<span class="material-symbols-outlined"> sdk </span>CohesionOptimizer Tool
</a>
<br>
<a href="/documents/pubs/ms-thesis-tool-manual.pdf">
<span class="material-symbols-outlined"> developer_guide </span>Tool Manual
</a>
</div>



	
