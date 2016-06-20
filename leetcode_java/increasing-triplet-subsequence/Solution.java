public class Solution {
    public boolean increasingTriplet(int[] nums) {
       if(nums==null||nums.length<3){
           return false;
       }
       int len=nums.length;
       int min=Integer.MAX_VALUE,mid=Integer.MAX_VALUE;
       for(int i = 0 ;i < len ; i++){
           if(min > nums[i]){
               min = nums[i];
           } else if( nums[i] > min){
               if(mid < nums[i] ){
                   return true;
               }
                mid = nums[i];
           }
       }
       return false;
    }
}