public class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;
        for(int i = 2; i <= n; i++) dp[i] = dp[i-1] + dp[i-2];
        return dp[n];
    }
}

public class Solution {
    public int climbStairs(int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        
        int[] step = new int[Math.max(n + 1, 3)];
        
        
        step[0] = 0;
        step[1] = 1;
        step[2] = 2;
        
        for(int i = 3; i <= n; i++){
            step[i] = step[i - 1] + step[i - 2];
        }
        
        return step[n];
    }
}