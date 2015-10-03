public class Solution {
    public int maxSubArray(int[] nums) {
        int res = Integer.MIN_VALUE, tmp = 0;
        for(int i = 0; i < nums.length; i++){
            tmp = Math.max(nums[i], tmp + nums[i]);
            res = Math.max(res, tmp);
        }
        return res;
    }
}

public class Solution {
    public int maxSubArray(int[] A) {
        
        int max = A[0];
        int history = A[0];
        
        for(int i = 1; i < A.length; i++){
            if(history < 0){
                history = A[i];
            }else{
                history += A[i];
            }
            
            max = Math.max(max, history);
            
        }
        
        return max;
    }
}
