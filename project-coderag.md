---
layout: page
title: CodeContext Explorer - CatBoost Code Explanation with RAG on Zillow Data
---

<div style="font-family: 'Alata'; font-size: small;">
<span>Aftab Hussain<br></span>

<span style="color: gray;">
  <br> <span class="material-symbols-outlined" style="font-size: 13pt;">calendar_clock</span> 
August 2025  </span> 
<br> 

<br>
<span class="material-symbols-outlined" style="font-size: 13pt; color: #d6ac16;">construction</span>  
Skills used:<span style="color: gray; font-size: small;">  LangChain framework, FAISS vector search, Flask web development, Mistral-7B-Instruct integration</span>

<br>
<br>

<a href="../Projects-pilot/index.html#coderag-menu"><span class="material-symbols-outlined" style="color: #1ba2d6; font-size: 13pt;">arrow_back</span><b>Return to Projects</b></a>
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

<img src="../images/projects/coderag/coderag.jpg" alt="drawing"/>

In this exploratory work, a Retrieval-Augmented Generation (RAG) system, CodeContext Explorer, is built to provide code explanations aimed at demonstrating the potential of combining RAG techniques with domain-specific code context. In this work, housing-data-related code is picked, in particular CatBoost code snippets applied to housing datasets (e.g. Zillow). CodeContext Explorer enables users to query contextualized code examples and their descriptions, supporting better understanding and usage of CatBoost in real estate modeling tasks.

The system relies upon synthetically created CatBoost code samples, used in the domain of housing data, with descriptive annotations. Using vector embeddings and a FAISS index, it retrieves the most relevant code-context pairs in response to user queries. These retrieved contexts are passed to the Mistral-7B-Instruct language model with custom prompts to generate explanations.

Results are stored in JSON format and presented through an interactive Flask web interface, allowing easy browsing of questions, related code snippets, and explanations — facilitating learning and exploration for data scientists and ML practitioners.

_________________


<div style="font-family: 'Alata'; font-size: small;">
<b>
<a href="https://github.com/AftabHussain/catboost-code-rag">
<span class="material-symbols-outlined"> code_blocks </span>Source code - Github
</a>
</b>
</div>

_____________


	
