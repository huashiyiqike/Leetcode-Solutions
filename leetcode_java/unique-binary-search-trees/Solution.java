public class Solution {
    public int numTrees(int n) {
        int dp[] = new int[n+1];
        dp[0] = 1;
        for(int i = 0 ;i <= n; i++){
            for(int j = 0; j < i; j++) {
                dp[i] += dp[j]*dp[i-1-j];
            }
        }
        return dp[n];
    }
}

public class Solution {
    public int numTrees(int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        if(n == 0) return 1;
        
        int s = 0;
        
        for(int i = 0; i < n; i++){
            s += numTrees(i) * numTrees(n - 1 - i);
        }
        
        return s;
    }
}