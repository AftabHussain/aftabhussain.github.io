---
layout: page
title: Projects 
---

<br>

<!-- Switch Button -->
<div class="switch-container">
    <label class="switch">
        <input type="checkbox" id="project-switch">
        <span class="slider"></span>
    </label>
    <span id="switch-text">&nbsp; Main/Pilot Projects</span>
</div>


<!-- Main Projects Section -->
<div id="main-projects">

<h2><a href="../project-code-intel/index.html" id="code-intel-menu">Safe and Explainable AI for Code</a></h2>

<div style="font-family: 'Alata';">
    <span style="font-size: small;">Aftab Hussain, Md Rafiqul Islam Rabin, Mohammad Amin Alipour, Vincent J. Hellendoorn, Bowen Xu, Omprakash Gnawali, Sen Lin, Toufique Ahmed, Premkumar Devanbu, Navid Ayoobi, David Lo, Sahil Suneja<br></span>
    <span style="color: gray; font-size: small;">University of Houston, Carnegie Mellon University, North Carolina State University, University of California, Davis, Singapore Management University, IBM Research <br>
    2021 to present <br></span>
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Deep Neural Models of Code</span>
</div>

<hr>

<h2><a href="../project-fuzz-enhance/index.html" id="fuzz-enhance-menu">Enhancing Fuzzing for Better Bug Detection and Triaging</a></h2>


<div style="font-family: 'Alata';">
    <span style="font-size: small;">Aftab Hussain, Mohammad Amin Alipour <br></span>
    <span style="color: gray; font-size: small;">University of Houston <br> 2020 to 2021 <br></span>
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Software Testing</span>
</div>

<hr>


<h2><a href="../project-glue-gen/index.html" id="glue-gen-menu">Glue Code Generation for Linux Kernel Security</a></h2>

<div style="font-family: 'Alata';">
    <span style="font-size: small;">Vikram Narayanan, Aftab Hussain, Anton Burtsev <br></span>
    <span style="color: gray; font-size: small;">University of California, Irvine <br> Supported by National Science Foundation <br> 2018 to 2019 <br></span>
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Kernel Security</span>
</div>

<hr>

<h2><a href="../project-idl-gen/index.html" id="idl-gen-menu">IDL Generation for Linux Kernel Security</a></h2>

<div style="font-family: 'Alata';">
    <span style="font-size: small;">Vikram Narayanan, Yongzhe Huang, Aftab Hussain, Anton Burtsev, Gang Tang, Trent Jaeger<br></span>
    <span style="color: gray; font-size: small;">University of California, Irvine, Penn State University
 <br> Supported by National Science Foundation <br> 2017 to 2019 <br></span>
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Kernel Security</span>
</div>

<hr>

<h2><a href="../project-graspan/index.html" id="graspan-menu">Graspan</a></h2>

<div style="font-family: 'Alata';">
    <span style="font-size: small;">Kai Wang, Aftab Hussain, Zhiqiang Zuo, Harry Xu, Ardalan
    Amiri Sani, John Thorpe, Sung-Soo Son, Khanh Ngyuen <br></span>
    <span style="color: gray; font-size: small;">University of California, Irvine 
    <br> Supported by National Science Foundation, ACM<br>2015 to 2017<br></span>
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Big Data Systems</span>
</div>

<hr>

<h2><a href="../project-query-sof/index.html" id="query-sof-menu">From Query to Usable Code - An Analysis of Stack Overflow Code Snippets</a></h2>

<div style="font-family: 'Alata';">
    <span style="font-size: small;">Di Yang, Aftab Hussain, Cristina Lopes <br></span>
    <span style="color: gray; font-size: small;">University of California, Irvine 
    <br> Supported by National Science Foundation<br>2013 to 2015<br></span>
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Mining Software Repositories</span>
</div>

<hr>

<h2><a href="../project-kw-sw/index.html" id="kw-sw-menu">Software Restructuring using Hierarchical Clustering</a></h2>

<div style="font-family: 'Alata';">
    <span style="font-size: small;">Aftab Hussain, Md. Saidur Rahman <br></span>
    <span style="color: gray; font-size: small;">Bangladesh University of Engineering and Technology <br> Supported by CodeCrafters International<br>2011 to 2013<br></span> 
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">Software Clustering</span>
</div>

</div>

<!-- Pilot Projects Section -->
<div id="pilot-projects">

<h2><a href="../project-fuzz-enhance/index.html">(To be added)</a></h2>

<div style="font-family: 'Alata';">
    <span style="font-size: small;">To be added <br></span>
    <span style="color: gray; font-size: small;">to be added <br> to be added <br></span>
    <span class="material-symbols-outlined" style="color: #1ba2d6;">label</span>
    <span style="color: #1ba2d6; font-size: small;">To be added</span>
</div>

<hr>


</div>


<script>
document.getElementById('project-switch').addEventListener('change', function() {
    var mainProjects = document.getElementById('main-projects');
    var pilotProjects = document.getElementById('pilot-projects');
    var switchText = document.getElementById('switch-text');
    if (this.checked) {
        mainProjects.style.display = 'none';
        pilotProjects.style.display = 'block';
        switchText.innerText = 'Pilot Projects';
    } else {
        mainProjects.style.display = 'block';
        pilotProjects.style.display = 'none';
        switchText.innerText = 'Main Projects';
    }
});
</script>

<style>
.switch-container {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

.switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
}

.switch input {
    opacity: 0;
    width: 0;
    height: 0;
}

.slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #1ba2d6;
    transition: .4s;
    border-radius: 34px;
}

.slider:before {
    position: absolute;
    content: "";
    height: 26px;
    width: 26px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    transition: .4s;
    border-radius: 50%;
}

input:checked + .slider {
    background-color: #1ba2d6;
}

input:checked + .slider:before {
    transform: translateX(26px);
}

#switch-text {
    margin-left: 10px; 
    font-family: 'Alata';
    font-size: 13pt;
    color: #333;
}
</style>
														



	
