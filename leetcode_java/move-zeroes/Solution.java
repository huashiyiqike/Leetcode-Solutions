public class Solution {
    public void moveZeroes(int[] nums) {
        int zeros = 0, idx = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 0) zeros++;
            else nums[idx++] = nums[i];
        }
        for(; idx < nums.length;idx++) nums[idx] = 0;
    }
}