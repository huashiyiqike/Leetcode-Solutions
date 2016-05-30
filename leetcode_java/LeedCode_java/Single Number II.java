/*
Given an array of integers, every element appears three times except for one. Find that single one. 
*/

public class Solution {
    public int singleNumber(int[] nums) {
        int len = nums.length;
        int result = 0;
        int[] count = new int[32];
        for(int i = 0;i < 32; i++){
            for(int j = 0;j < len; j++){
                if(((nums[j]>>i) & 1)==1){
                    count[i]++;
                }
            }
           result| = ((count[i]%3)<<i);
        }
        return result;
    }
}