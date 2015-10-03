public class Solution {
    public int minDistance(String word1, String word2) {
        char[] a = word1.toCharArray(), b = word2.toCharArray();
        int[][] dp = new int[a.length+1][b.length+1];
        for(int i = 0; i < a.length+1; i++){
            for(int j = 0; j < b.length+1; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        for(int i = 0; i < a.length+1; i++) dp[i][0] = i;
        for(int j = 0; j < b. length+1; j++) dp[0][j] = j;
        for(int i = 1; i < a.length+1; i++){
            for(int j = 1; j < b.length+1; j++){
                if(a[i-1] == b[j-1]) dp[i][j] = dp[i-1][j-1];
                else dp[i][j] = 1+ Math.min(dp[i-1][j-1],Math.min(dp[i][j-1], dp[i-1][j]));
            }
        }
        return dp[dp.length-1][dp[0].length-1];
    }
}
public class Solution {
    public int minDistance(String word1, String word2) {
        
        // http://en.wikipedia.org/wiki/Levenshtein_distance
        
        char[] w1 = word1.toCharArray();
        char[] w2 = word2.toCharArray();
        

        
        int[][] P = new int[w1.length + 1][w2.length + 1];
        
        int i, j;
        
        for(i = 1; i <= w1.length; i++){
            P[i][0] = i;
        }
        
        for(j = 1; j <= w2.length; j++){
            P[0][j] = j;
        }
        
        for(i = 1; i <= w1.length; i++){
            for(j = 1; j <= w2.length; j++){
                
                P[i][j] = Math.min(P[i - 1][j], P[i][j - 1]) + 1;
                
                if(w1[i - 1] == w2[j - 1]){
                    P[i][j] = Math.min(P[i - 1][j - 1], P[i][j]);
                }else {
                    P[i][j] = Math.min(P[i - 1][j - 1] + 1, P[i][j]);
                }
                
            }
        }
        
        return P[w1.length][w2.length];
    }
}