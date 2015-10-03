public class Solution {
    public int rob(int[] nums) {
        int[] dp = new int[nums.length];

        if(nums.length == 0) return 0;
        else if(nums.length == 1) return nums[0];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        for(int i = 2; i < dp.length; i++){
            dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]);
        }
        return dp[dp.length-1];
    }
}

public class Solution {
    public int rob(int[] num) {
        if(num.length == 0) return 0;
        if(num.length == 1) return num[0];
        
        int[] P = new int[num.length];
        
        P[0] = num[0];
        P[1] = Math.max(num[0], num[1]);

        for(int i = 2; i < num.length; i++){
            P[i] = Math.max(num[i] + P[i - 2], P[i - 1]);
        }
        
        return P[num.length - 1];
    }
}
