>Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.

We can sort the array and save the according index to a new array. Iterating through this new array, we get an ascending array.  The first requirement is difference of value below t; we use that to stop inner iteration. The second requirement is difference of index below k; we check that and once true return true.

