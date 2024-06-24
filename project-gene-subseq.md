---
layout: page
title: An ML Framework for Gene Subsequence Analysis
---

<div style="font-family: 'Alata'; font-size: small;">
<span>Aftab Hussain<br></span>

<span style="color: gray;">
  University of Houston
  <br> <span class="material-symbols-outlined" style="font-size: 13pt;">calendar_clock</span> 
2024 to present </span> 
<br> 

<br>
<span class="material-symbols-outlined" style="font-size: 13pt; color: #d6ac16;">construction</span>  
Skills used:<span style="color: gray; font-size: small;">  Python, data manipulation, information retrieval</span>

<br>
<br>

<a href="../Projects-pilot/index.html#gene-subseq-menu"><span class="material-symbols-outlined" style="color: #1ba2d6; font-size: 13pt;">arrow_back</span><b>Return to Projects</b></a>
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

<img src="../images/projects/gene-subseq/back.jpg" alt="drawing"/>

This exploratory project aims to develop an approach to investigate the relationship between gene subsequences and gene families. We apply this approach to a curated synthetic dataset consisting of 50,000 samples, each containing a pair of a gene sequence and its corresponding family. Our goal is to create a machine learning framework to determine if there are relationships between certain features of gene subsequences and the families of genes.

Specifically, we construct the feature Subs\_k\_N, which represents the number of subsequences in a gene sequence where the total number of nucleotides of type N is k. To compute this feature for each nucleotide, we utilize a hash-map-based prefix-sum approach with a complexity of O(n), where n is the number of characters in the given sample.

Our framework leverages multiple machine learning algorithms to thoroughly investigate this relationship, providing insights into the connections between gene subsequences and their families.

_________________


<div style="font-family: 'Alata'; font-size: small;">
<b>
<a href="https://github.com/AftabHussain/gene-subseq-analysis">
<span class="material-symbols-outlined"> code_blocks </span>Source code - Github
</a>
</b>
</div>

_____________

<p style="color:gray;font-size:8pt;"><small><a href="https://www.freepik.com/free-vector/dna-genetic-biotechnology-science-vector-purple-neon-graphic_16396002.htm#fromView=search&page=2&position=0&uuid=ed02a6ad-c96c-4f14-a5af-9b3349ef4177" target="_blank">Image by rawpixel.com on Freepik</a></small></p>


	