<backquote><pre>
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
</backquote></pre>

Almost same as "Search in Rotated Sorted Array", except  that because of the duplicates, we cannot easily decide whether a part is sorted. The decision is made by testing if nums[mid] <= nums[r], but it is possible the condition is true but the part is not sorted, e.g. [1,1,3,1]. So if the target is not in the leftmost or the rightmost part, we cannot remove that as a whole, but one by one.