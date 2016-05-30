/*
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.

Subscribe to see which companies asked this question
*/

public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        boolean flag=false;
        if (k < 1 || t < 0)
		return false;
        if(nums==null||nums.length==0||nums.length==1){
            return flag;
        }
        int j;
        TreeSet<Long> set=new TreeSet<Long>();
        int len=nums.length;
            for(j=0;j<len;j++){
             long leftBoundary = (long) nums[j] - t;
		long rightBoundary = (long) nums[j] + t + 1;
		SortedSet<Long> subSet = set.subSet(leftBoundary, rightBoundary);
 
		if (!subSet.isEmpty())
			return true;
 
		set.add((long) nums[j]);
 
		if (j >= k) {
			set.remove((long) nums[j - k]);
		}
            }
        return flag;
    }
}