public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int min = Integer.MAX_VALUE;
        int result = 0;
        int len = nums.length;
        int j ,k ;
        
        int diff;
        int sum = 0;
        Arrays.sort(nums);
        for(int i  = 0; i < len ;i++){
            j = i + 1;
            k = len -1 ;
            while(j < k){
                sum = nums[i] + nums[j] + nums[k];
                diff = Math.abs(sum - target);
                if(diff == 0){
                    return sum;
                }
                if(diff < min){
                    min = diff;
                    result = sum;
                }
                if(sum < target){
                    j++;
                }else{
                    k--;
                }
            }
        }
        return result;
    }
}