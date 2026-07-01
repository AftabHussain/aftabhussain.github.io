# Sorting Stability

A sorting algorithm is stable if it preserves the relative order of equal elements.

## One-line definition 

Stable sort: equal keys keep their original order after sorting.

## Tiny example

### Original list (key, label):

(5, A), (3, B), (5, C)


### Sorted by key:

Stable sort →

(3, B), (5, A), (5, C)


### Unstable sort →

(3, B), (5, C), (5, A)   ❌ order changed


The values are sorted either way — only stability cares about A before C.

## Why stability matters

Multi-key sorting (e.g., sort by last name, then first name)

Preserving semantic order (timestamps, IDs)

Databases, UI tables, logs

## Quick rule of thumb

Stable: Merge Sort, Insertion Sort, Bubble Sort, TimSort

Unstable: Quick Sort, Heap Sort, Selection Sort

## One line summary

“Stability doesn’t affect correctness of sorting, but it affects whether equal elements keep their original semantic order.”
