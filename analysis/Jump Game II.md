<backquote><pre>
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
</backquote></pre>

DP:
We can use a dp array to record the minimum steps at each index of the given array. If the current maximum place (equals current index plus the element at that spot) is greater than previous maximum place, we can set all the elements in the dp array between the previous max and the current max to 1 + previous dp value, and then update the maximum place.

Space efficient way:
Just keep record of the last maximum jump start, and maximum place within reach, cur. If cur is greater than the length of array, we are done. Otherwise we continue to see if we can jump further from previous  position to current position. If so, record that value and either way we shoud update the maximum jump start and cur, and increase the steps taken by 1.

