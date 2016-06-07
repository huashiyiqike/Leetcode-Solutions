<backquote><pre>
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
</backquote></pre>

There are two ways to tackle this problem.
1. treat this rotated sorted array as a sorted array. We use the first element as the target and return the first one smaller than it. If we cannot find that, we return the first element as the smallest.
2. we compare the middle with the rightmost to see if the right part is sorted. If so, we can safely remove the right part; otherwise we know the smallest is in the right part so we remove the left part.