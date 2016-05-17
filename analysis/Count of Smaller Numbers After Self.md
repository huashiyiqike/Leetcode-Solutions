<backquote><pre>
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
</pre>
</backquote>

"The gist of this solution is to start from the end and keep a sorted array of numbers that have already occurred. When inserting the current number, the index at which you insert the number into the array corresponds to how many numbers are smaller to the right of it." 