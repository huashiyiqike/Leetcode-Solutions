/*
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5]. 
*/

public class Solution {
    public int[] singleNumber(int[] nums) {
        int len = nums.length ;
        int res = 0 ;
        for(int i = 0;i < len; i++){
            res = (res^nums[i]);
        }
        int first_diff_bit=0;
        for(int i = 0;i < 32; i++){
            if(((res>>i) & 1)==1){
                first_diff_bit=i;
                break;
            }
        }
        int first=0;
        for(int i=0;i<len;i++){
            if(((nums[i]>>first_diff_bit) & 1)==1){
                first=(first^nums[i]);
            }
        }
        int[] result = new int[2];
        result[0] = first;
        result[1] = first^res;
       return result;
    }
}