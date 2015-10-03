public class Solution {
    public int rob(int[] nums) {
        if(nums.length == 0) return 0;
        else if(nums.length == 1) return nums[0];
        else if(nums.length == 2) return Math.max(nums[0], nums[1]);

        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = nums[0];
        for(int i = 2; i < nums.length-1; i++){
            dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]);
        }
        int max1 = dp[dp.length-2];

        for(int i = 0; i < dp.length; i++) dp[i] = 0;
        dp[0] = 0;
        dp[1] = nums[1];
        for(int i = 2; i < nums.length; i++){
            dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]);
        }
        return Math.max(max1, dp[dp.length-1]);
    }
}

public class Solution {

    // rob1
    int rob(int[] num, int st, int len) {
        if(len == 0) return 0;
        if(len == 1) return num[st + 0];

        int[] P = new int[len];

        P[0] = num[st + 0];
        P[1] = Math.max(num[st + 0], num[st + 1]);

        for(int i = 2; i < len; i++){
            P[i] = Math.max(num[st + i] + P[i - 2], P[i - 1]);
        }

        return P[len - 1];
    }

    public int rob(int[] nums) {

        if(nums.length == 0) return 0;
        if(nums.length == 1) return nums[0];

        return Math.max(rob(nums, 0, nums.length - 1), rob(nums, 1, nums.length - 1));
    }
}
