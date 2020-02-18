---
layout: page
title: Deconstructring Implementations of some Sorting Algorithms
---

<small>Aftab Hussain <br><font color="gray">February 17, 2020</font>
<br><b><a href="../Tech-blog/index.html#ds-and-algo"><small><i class="fa fa-tag" style="font-size:15px"></i>&nbsp;&nbsp;DATA STRUCTURES AND ALGORITHMS</small></a></b></small>
<hr>

<link href="https://fonts.googleapis.com/css?family=Source+Code+Pro:500&display=swap" rel="stylesheet">
<style>
/*Source+Code+Pro:500&display=swap*/
code { 
  font-family: "Source Code Pro";
  font-size:90%
}
pre code { 
  font-family: "Source Code Pro";
  font-size:110%
}
pre {
  background-color: #EAEADF;
}
/*#E6EEEC*/
</style>

## **Merge Sort**
<br>
There are various ways to implement the popular merge sort algorithm, a [divide-and-conquer algorithm](https://www.wikiwand.com/en/Divide-and-conquer_algorithm) with an average time complexity of *O(nlogn)* and a worst case space complexity of *O(n)*. Among the variants include
the top-down variant, and the bottom up variant. The *bottom up* implementation takes in the input as an array of 
`n` sublists of size 1, and iteratively merges sub-lists back and forth between two buffers. Whereas, the *top down* approach begins by recursively splitting the input list into sublists until the size of a sublist is 1. Then, it merges those sublists to produce a sorted list [1]. Here, we go over the top down version.

## Preliminary Considerations
The idea is pretty simple. Let's touch upon some details which we can identify right away. 

First, given any list of size 0, or 1, we don't need to bother about it, and can go home, 
regardless of which sorting algorithm we want to use. 

With the base case dealt with, we notice that a key operation in the merge sort procedure is splitting. 
We can use the median element in the array to split, based on which we get equal sized sub-arrays 
if the number of elements in the array that we are splitting is even, or unequal ones if the number is odd.

The merge_sort function would thus need three arguments: the array, the lowest index, and the highest index.

Let's get started coding in C++ by having a function that accepts an array to sort from the user, and prints out the
sorted array. We can use this for other sorting algorithms too, except the line of the sort function call would change
depending on what arguments it takes:

```cpp
#include<iostream>
using namespace std;

void main() {
  int arr[100], num;
  cout<<"# of ints to sort? (< 101)"<<endl;
  cin>>num;
  cout<<"Enter the elements"<<endl;
  for (int i=0; i < num; i++){
    cin>>arr[i];
  } 

  if(num > 1) // catering for base case
    // don't forget the -1 to get highest index
    merge_sort(arr, 0, num-1); 

  cout<<"The sorted array is:"<<endl;
  for (int i=0; i < num; i++){
    cout<<arr[i];
  } 
  cout<<endl;
}
```

## Splitting
Now let's begin writing our `merge_sort()` function, and get the median index.

```cpp
merge_sort(int * arr, int low, int high){
  int mid = (low + high) / 2;
```

Giving us the median allows us to recursively call `merge_sort()` on the two subparts, which we do
next:

```cpp
  ...
  merge_sort(arr, low, mid);
  merge_sort(arr, mid+1, high);
```
The above is essentially the splitting step of the algorithm. But wait. 

The algorithm will not go beyond these
two instructions, if we leave them as they are. We want to split the array, until we have split the array 
to singletons. Then we'd like to move on to merging them. How do we stop this recursive splitting process
once we have reached singletons? 

We could use our `low` and `high` values. For an array with one element, 
these two values would be equal. So we'd like to do all this while `low` is less than `high`. It also 
makes sense to get the median, only if such is the case. Hence modifying the above, we get, 

```cpp
merge_sort(int * arr, int low, int high){
  if (low < high){
    int mid = (low + high) / 2;
    merge_sort(arr, low, mid);
    merge_sort(arr, mid+1, high);
```

Once we have reached singletons, the final step we'd like to do is to start merging the elements
back together. It is during this merge that the sorting is applied. This step is in fact, the trickiest
and the most tedious part of the procedure. Let's encapsulate this step inside the function `merge`, which 
we shall from `merge_sort`, right after recursively splitting the subparts (using `merge_sort`).
```cpp
merge_sort(int *arr, int low, int high){
  if (low < high){
    ...
    merge(arr, low, mid, high);
  }
}
```
This completes the implementation of the `merge_sort` function. As we can see we have passed all three
indexes to the merge function. These will come in handy as we can soon see for tracking purposes during the 
merging process.

## The Merging Process
The idea is pretty straight-forward, but we have to be careful which is why it is tricky. Basically, start scanning 
your two sub-arrays, comparing one element from each array with one another, sequentially. 
Whichever is smaller, store it in a temporary array. The temporary array would be of the same size as the whole array.
Let's set up the temporary array:
```cpp
void merge(int *arr, int low, int mid, int high) {
  int temp[high - low + 1]; //dealing with indexes, so add 1

```
During the scanning process, use trackers to keep track of where you are 
at. Take a look below on the trackers you'll need:

```
   low      mid  mid+1       high     | Src array anchors
[   a , .. , e ,   f   , .. , n   ]   | Src array (unsplit)
    i-->           j-->	              | Src array trackers

[   a , .. .. .. .. .. . .. , n   ]   | Temp array
    k-->		              | Temp array tracker
```

The source array is the array that was split. This whole source array is passed
to the `merge` function. The `low`, `mid`, `high` indexes of this array provides us
the split information for this array. `i` and `j` will be used to iteratively 
scan each of the subparts of the array, where they start in the 
positions as shown above. The smaller element is stored in the temporary array,
tracked by `k`. So continuing our `merge` function,

```cpp
  ...
  int i = start, j = mid+1, k = 0;
```

As we store elements into the temporary array, a number of things happen: 
first, we increment tracker `k`.  Second, `i` *or* `j` is incremented
(not both), depending on which of the tracker's element was stored.

Let's kick off the scanning and storing now.
<br><small>(We may copy the input array to the `merge` function 
into separate arrays during this merge process as was 
done [here (the C version)](https://www.geeksforgeeks.org/merge-sort/). However,
in this implementation we shall use the same input array, as the indexes are sufficient.)

```cpp
  while(i <= mid && j <= high){
    if (arr[i]<=arr[j]){
      temp[k] = arr[i];
      k++; i++;
    } 
    else {
      temp[k] = arr[j];
      k++; j++;
    }
  }
```

Wait, we are not done yet. We may have elements left in the subarrays
that are yet to be copied in to the temporary array. Let's get them in the temporary
array:
```cpp
  ...
  while (i <= mid){
      temp[k] = arr[i];
      k++; i++;
  }
  while (j <= high){
      temp[k] = arr[i];
      k++; i++;
  }
```
Finally, copy the temporary array into the main array and we are done:
```
  for (int x = 0; x < end; x++){
    arr[x] = temp[x];
  }
```
(Arrays are passed by reference, so there's no need for our functions to return anything).

<hr>

## **Quick Sort**
<br>
This is another divide-and-conquer algorithm with an average case time complexity of *O(nlog(n))*, but with a better worst case space complexity of *O(log(n))*.


<hr>

## **Heap Sort**
<br>
    
## Example

Using the default settings, say we created a file `testfile.txt`. Here are the permission info:



<hr>

<b>References:</b>
<br><small>1. [Merge sort, Wikipedia](https://www.wikiwand.com/en/Merge_sort)</small>
<br><small>2. [Merge sort algorithm, InterviewBit](https://www.interviewbit.com/tutorial/merge-sort-algorithm/)</small>
<br><small>3. [Merge Sort In C++ With Examples, Software Testing Help](https://www.softwaretestinghelp.com/merge-sort/)</small>





