<backquote><pre>
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
</backquote></pre>

How to use binary search on a rotated array? If we can be sure the part is sorted, it will be easy. The best practice is to narrow down the residual by eliminating either the leftmost part or the rightmost part because they tend to be sorted and it is easier for us to move pointers. 