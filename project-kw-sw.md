---
layout: page
title: Software Restructuring using Hierarchical Clustering
---

<div style="font-family: 'Alata'; font-size: small;">
<span>Aftab Hussain, Md. Saidur Rahman   <br></span>
<span style="color: gray;">Graph Drawing and Information Visualization Lab
<br> Department of Computer Science and Engineering 
<br> Bangladesh University of Engineering and Technology  
<br> Supported by a href="https://www.codecraftersintl.com/">CodeCrafters International</a>
<br>  <a href="https://2016.msrconf.org/#/home">6th India Software Engineering Conference 2013 (ISEC 2013), New Delhi, India</a></span> 
<br>
<br>
<a href="../Projects/index.html#kw-sw-menu"><span class="material-symbols-outlined" style="color: #1ba2d6; font-size: 13pt;">arrow_back</span><b>Return to Projects</b></a>
<br>
<br>
</div>


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

● Invited for presentation in Workshop on Graph Drawing and Graph Algorithms (GDGA) 2013, Bangladesh University of Engineering and Technology.  

_________________________

<div style="font-family: 'Alata'; font-size: small;">
<a href="https://dl.acm.org/doi/10.1145/2442754.2442761">
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



	
