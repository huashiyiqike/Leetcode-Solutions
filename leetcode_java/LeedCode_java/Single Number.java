/*
Given an array of integers, every element appears twice except for one. Find that single one.
*/

public class Solution {
    public int singleNumber(int[] nums) {
       int len = nums.length;
       int result = nums[0];
       for(int i = 1;i < len; i++){
           result = (result ^ nums[i]);
       }
       return result;
    }
}