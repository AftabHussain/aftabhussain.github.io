---
layout: page
title: Shared Resources
---

- [Research](#research) 
- [Teaching](#teaching)

  <!-- https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_sort_table_desc-->

## Research
<small>*Click on headers to sort.*</small>

<table id="rch">
  <tr>
   <!--When a header is clicked, run the sortTable function, with a parameter, 0 for sorting by names, 1 for sorting by country:-->  
    <th onclick='sortTable(0,"rch")'>Item&nbsp;<i class="fa fa-sort" style="font-size:20px"></i></th>
    <th onclick='sortTable(1,"rch")'>Date&nbsp;<i class="fa fa-sort" style="font-size:20px"></i></th>
  </tr>
  <tr>
    <td><a href="https://gitlab.flux.utah.edu/xcap/xcap-capability-linux/tree/dev_idl_4.8/tools/lcd/idl">Source code - IDL compiler</a> (under development)</td>
    <td>2018</td>
  </tr>
  <tr>
    <td><a href="https://github.com/AftabHussain/DataStructureAnalysis/tree/dsa_llvm3.8">Source code - IDL generator</a> (under development)</td>
    <td>2018</td>
  </tr>  
  <tr>
    <td><a href="/documents/pubs/asplos17-graspan.pdf">Paper - Graspan graph processing system ASPLOS 2017</a></td>
    <td>2017</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Graspan/graspan-java">Source code - Graspan graph processing system</a></td>
    <td>2017</td>
  </tr> 
  <tr>
    <td><a href="/documents/pubs/asplos17-graspan-poster.pdf">Poster - Graspan graph processing system ASPLOS 2017</a></td>
    <td>2017</td>
  </tr>  
</table>

## Teaching <a href="#top">⬆</a>  {#teaching}
<small>*Click on headers to sort.*</small>

<table id="tch">
  <tr>
   <!--When a header is clicked, run the sortTable function, with a parameter, 0 for sorting by names, 1 for sorting by country:-->  
    <th onclick='sortTable(0,"tch")'>Item&nbsp;<i class="fa fa-sort" style="font-size:20px"></i></th>
    <th onclick='sortTable(1,"tch")'>Date&nbsp;<i class="fa fa-sort" style="font-size:20px"></i></th>
  </tr>
  <tr>
    <td><a href="/documents/teaching/uci/cs238p/fall2018/discussions/discussion01-shell-vim.pdf">Lecture slides - Operating Systems Fall 2018 Discussion 01 - Basic shell commands</a></td>
    <td>2018/10/05</td>
  </tr>
</table>

<script>
function sortTable(n,name) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById(name);
  switching = true;
  //Set the sorting direction to ascending:
  dir = "asc"; 
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /*check if the two rows should switch place,
      based on the direction, asc or desc:*/
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      //Each time a switch is done, increase this count by 1:
      switchcount ++;      
    } else {
      /*If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again.*/
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
</script>

