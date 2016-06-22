public class Solution {
    public void wiggleSort(int[] nums) {
      Arrays.sort(nums);
      int len = nums.length;
      int mid = (len%2 == 0 )?(len/2-1):len/2;
      int index = 0;
      int[] arr = new int[len] ;
      for(int i = 0 ;i <= mid ;i++){
          arr[index] = nums[mid-i];
          if((index + 1) < len){
              arr[index+1] = nums[len-i-1];
          }
          index = index+2;
      }
      for(int i = 0 ; i < len ;i++){
          nums[i] = arr[i];
      }
   }
}