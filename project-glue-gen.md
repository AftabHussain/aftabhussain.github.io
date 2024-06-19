---
layout: page
title: Glue code generation for Linux Kernel Security
---

<div style="font-family: 'Alata'; font-size: small;">
<span>Vikram Narayanan, Aftab Hussain, Anton Burtsev   <br></span>
<span style="color: gray;">
Mars Systems
<br> Department of Computer Science
<br> University of California, Irvine 
<br> 
<br> <span class="material-symbols-outlined" style="font-size: 13pt;">account_balance</span> Supported by <a href="https://www.nsf.gov/">National Science Foundation</a>
<br> <span class="material-symbols-outlined" style="font-size: 13pt;">event</span> Accepted at <a href="https://www.usenix.org/conference/atc19/presentation/narayanan">The 2019 USENIX Annual Technical Conference (USENIX ATC 2019)
Renton, Washington</a></span> 

<br>
<span class="material-symbols-outlined" style="font-size: 13pt; color: #d6ac16;">construction</span>  
Skills used:<span style="color: gray; font-size: small;">  C, C++, compilers</span>

<br>
<br>
<a href="../Projects/index.html#glue-gen-menu"><span class="material-symbols-outlined" style="color: #1ba2d6; font-size: 13pt;">arrow_back</span><b>Return to Projects</b></a>
<br>
<br>
</div>


Generated glue code from IDL syntax for Linux kernel security using
vembyr code parser generator.

- Contributed towards implementing an Interface Definition Language that
  captures decomposition patterns typically used in the kernel such as exported
functions, data structures passed by reference, function pointers, etc.

- Contributed towards the development of an IDL compiler that can generate the
  runtime glue-code required for decomposition – The compiler works as a
source-to-source translator from the LXD IDL to C.

_________________________

<div style="font-family: 'Alata'; font-size: small;">
<b>
<a href="/documents/pubs/lxds-usenix19.pdf">
<span class="material-symbols-outlined"> article </span>Paper - USENIX 2019
</a>
<br>
<a href="https://gitlab.flux.utah.edu/xcap/xcap-capability-linux/tree/dev_idl_4.8_no_channels/tools/lcd/idl">
<span class="material-symbols-outlined"> code_blocks </span>Source code - Gitlab
</a>
<br>
<a href="https://gitlab.flux.utah.edu/xcap/xcap-capability-linux/wikis/idl-compiler-documentation">
<span class="material-symbols-outlined"> description  </span>IDL Compiler Documentation
</a>
</b>
</div>


	
