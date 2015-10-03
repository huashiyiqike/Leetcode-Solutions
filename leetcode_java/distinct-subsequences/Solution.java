public class Solution {
    public int numDistinct(String s, String t) {
        int[][] dp = new int[s.length()+1][t.length()+1];
        char[] a = s.toCharArray();
        char[] b = t.toCharArray();
        for(int i = 0; i < s.length()+1; i++){
            for(int j = 0; j < t.length()+1; j++) {
                dp[i][j] = 0;
                if(j == 0) dp[i][j] = 1;
            }
        }
        for(int i = 1; i < s.length()+1; i++){
            for(int j = 1; j < t.length()+1; j++){
                dp[i][j] += dp[i-1][j];
                if(a[i-1] == b[j-1]){
                    dp[i][j] += dp[i-1][j-1];
                }
            }
        }
        return dp[s.length()][t.length()];
    }
}

public class Solution {
    public int numDistinct(String S, String T) {
        
        
        char[] s = S.toCharArray();
        if(s.length == 0) return 0;
        
        char[] t = T.toCharArray();
        if(t.length == 0) return 0;
        
        if(t.length > s.length) return 0;
        
        
        int[][] P = new int[s.length][t.length];
        
        
        P[0][0] = s[0] == t[0] ? 1 : 0;
        
        for(int i = 1; i < s.length; i++){
            P[i][0] = s[i] == t[0] ? 1 + P[i - 1][0] : P[i - 1][0]; 
        }
        
        
        for(int j = 1; j < t.length; j++){
            for(int i = j; i < s.length; i++){
                
                if(t[j] == s[i]){
                    // sum choices
                    
                    P[i][j] = P[i - 1][j] + P[i - 1][j - 1];
                    
                    
                } else {
                    // no choice
                    P[i][j] = P[i - 1][j];
                    
                }
                
                
                
                
            }
        }
        
        
        return P[s.length - 1][t.length - 1];
        
        
    }
}