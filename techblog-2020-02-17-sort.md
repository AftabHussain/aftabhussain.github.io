---
layout: page
title: Deconstructring Implementations of Merge Sort and Quick Sort
---

<small>Aftab Hussain <br><font color="gray">February 17, 2020</font>
<br><b><a href="../Tech-blog/index.html#ds-and-algo"><small><i class="fa fa-tag" style="font-size:15px"></i>&nbsp;&nbsp;DATA STRUCTURES AND ALGORITHMS</small></a></b></small>
<hr>

<link href="https://fonts.googleapis.com/css?family=Source+Code+Pro:500&display=swap" rel="stylesheet">
<style>
/*Source+Code+Pro:500&display=swap*/
code { 
  font-size:90%;
}
pre code { 
  font-family: "Source Code Pro";
  font-size:110%;
  white-space: pre;
}
pre {
  background-color: #EAEADF;
  overflow: auto;
}
/*#E6EEEC*/
</style>

## **Merge Sort**
<br>
There are various ways to implement the popular merge sort algorithm, a [divide-and-conquer algorithm](https://www.wikiwand.com/en/Divide-and-conquer_algorithm) with an average time complexity of *O(nlogn)* and a worst case space complexity of *O(n)*. Among the variants include
the top-down variant, and the bottom up variant. 

The *bottom up* implementation takes in the input as an array of 
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

int main() {
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

Let's kick off the scanning and storing now. *(We may copy the input array to the `merge` function into separate arrays during this merge process as was done [here (the C version)](https://www.geeksforgeeks.org/merge-sort/). However, in this implementation we shall use the same input array, as the indexes are sufficient.)*

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
```cpp
  ...
  for (int x = 0; x < end; x++){
    arr[x] = temp[x];
  }
} //ignore this red mark-down highlight
```
(Arrays are passed by reference, so there's no need for our functions to return anything).

## The Complete Code in C++
```cpp
//https://www.interviewbit.com/tutorial/merge-sort-algorithm/
//https://www.softwaretestinghelp.com/merge-sort/
#include<iostream>
using namespace std;

void merge(int *arr, int low, int mid, int high) {
  int temp[high - low + 1]; //dealing with indexes, so add 1
  int i = start, j = mid+1, k = 0;
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
  while (i <= mid){
      temp[k] = arr[i];
      k++; i++;
  }
  while (j <= high){
      temp[k] = arr[i];
      k++; i++;
  }
  for (int x = 0; x < end; x++){
    arr[x] = temp[x];
  }
}

merge_sort(int * arr, int low, int high){
  if (low < high){
    int mid = (low + high) / 2;
    merge_sort(arr, low, mid);
    merge_sort(arr, mid+1, high);
    merge(arr, low, mid, high);
  }
}

int main() {
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

<hr>

## **Quick Sort**
<br>
This is another divide-and-conquer algorithm with an average case time complexity of *O(nlog(n))*, but with a better worst case space complexity of *O(log(n))*. Being a D&C algorithm, quick sort's idea is quite similar to merge sort's. 
Here, instead of picking a median element, we pick a random pivot element to split the array, and 
then sort the array such that elements to the pivot's left-side are smaller than (or equal to) the pivot, 
and all elements to the pivot's right are greater than the pivot. Then we apply the same procedure on 
each of the subarrays, recursively. During the sorting process we use a swapping procedure where we use 
a temporary variable. No new arrays are created in the process as all elements are sorted in-place, i.e., within 
the same array structure.

## Laying the foundations
Let's code up in C++ whatever we can based on the basic idea of the algorithm as discussed above:
```cpp
void quicksort(int *arr, int low, int high){
  //[function call to split the array]//
  //quicksort(partition 1)//
  //quicksort(partition 2)//
}
```
Okay, that turned out more like a pseudocode. We can tell `low` and `high` are obviously going to come in handy
for determining the array limits, hence we have it in the function. Since we'll be splitting the array 
over a pivot, these limits can be determined based on the pivot index. (`low` to `pivot index -1`) would give 
us the left partition, we can get the other from (`pivot index +1` to `high`). 
Let's grab these values:
```cpp
quicksort(int *arr, int low, int high){
  int pidx = split(arr, low, high);
```
Now let's use `pidx` to recursively invoke `quicksort` on the two partitions.
```cpp
  ...
  quicksort(arr, low, pidx-1);
  quicksort(arr, pidx+1, high);
}
```
So that completes our `quicksort` function right? No! This recursion would go on infinitely, we need to stop
splitting until we reach partitions of size 1, just as we did in mergesort. Add the stopping criterion:
```cpp
quicksort(int *arr, int low, int high){
  if (low < high) {
    int pidx = split_and_sort(arr, low, high);
    quicksort(arr, low, pidx-1);
    quicksort(arr, pidx+1, high);
  }
}
```
Now let the fun begin.
## Splitting and Moving Elements Around the Pivot

We use a trick here. It comes in three stages.

1. We pick the rightmost element of the array as a pivot. 

2. We iteratively swap around the other elements, depending on how each of them compare with the pivot element.
During this process we do not move the pivot element at all. (This is the most interesting stage.)

3. After we are done moving around all of these elements, the pivot element is swapped with *one* of these elements. We
shall call this element our *shadow pivot*. 

Following the final swap, we'll see that all elements are magically following the in-order pivot logic: all elements
to the left of our pivot would be less than (or equal to) the pivot, and all elements to the right of our
pivot would be greater than the pivot. (This final swap may not happen if the array is already ordered
in the in-order pivot logic after reordering the elements in stage 2.)

Stage 2 plays the central role for this trick in making it work. Those trackers come in handy again for this, 
so let's take a look at an example:
```
                                pidx	 | pivot index
[  2 ,  3  ,  23  ,  -1  ,  5  , 1  ]	 | array
 spidx--->				 | shadow pivot index
   i----->				 | array tracker
```
We set `spidx` and `i` to the start of the array, and `pidx`, to the end. We scan all 
elements apart from the pivot using `i`. For each scanned element if we see the element
is less than or equal to the pivot (pointed to by `pidx`), swap the shadow pivot and that element, 
and change the shadow pivot postion by pointing it to the next position (`spidx`++). This is the meat of 
the splitting logic (stage 2 above). Let's code up to here:
```cpp
void swap(int *i, int *j){
  int temp;
  temp=*i;
  *i = *j;
  *j = *temp;
}

int split_and_sort(int *arr, int low, int high) {
  int spidx=low;
  int pidx=high;
  for (int i=low; i<high; i++){
    //Note we compare with pivot, NOT shadow pivot
    //We only swap with shadow pivot
    if(arr[i]<=arr[pidx]){
      swap(&arr[i],&arr[spidx]);
      spidx++;
    }
  }
```
Our final task is to swap the pivot with the shadow pivot, and we are done:
```cpp
  ...
  swap(&arr[spidx],&arr[pidx]);
  pidx = spidx;
  return pidx; //don't forget to return the pivot
}
```
*(Please note a random pivot may also be used to implement quicksort.)*

## The Complete C++ Code

```cpp
//https://www.youtube.com/watch?v=COk73cpQbFQ
//https://www.geeksforgeeks.org/cpp-program-for-quicksort/

void swap(int *i, int *j){
  int temp;
  temp=*i;
  *i = *j;
  *j = *temp;
}

int split_and_sort(int *arr, int low, int high) {
  int spidx=low;
  int pidx=high;
  for (int i=low; i<high; i++){
    if(arr[i]<=arr[pidx]){
      swap(&arr[i],&arr[spidx]);
      spidx++;
    }
  }
  swap(&arr[spidx],&arr[pidx]);
  pidx = spidx;
  return pidx; //don't forget to return the pivot
}

void quicksort(int *arr, int low, int high){
  if (low < high) {
    int pidx = split_and_sort(arr, low, high);
    quicksort(arr, low, pidx-1);
    quicksort(arr, pidx+1, high);
  }
}
```
<hr>

<b>References:</b>
<br><small>1. [Merge sort, Wikipedia](https://www.wikiwand.com/en/Merge_sort)</small>
<br><small>2. [Merge sort algorithm, InterviewBit](https://www.interviewbit.com/tutorial/merge-sort-algorithm/)</small>
<br><small>3. [Merge Sort In C++ With Examples, Software Testing Help](https://www.softwaretestinghelp.com/merge-sort/)</small>
<br><small>4. [Quicksort, mycodeschool](https://www.youtube.com/watch?v=COk73cpQbFQ)</small>





