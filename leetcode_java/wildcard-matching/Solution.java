public class Solution {
    public boolean isMatch(String s, String p) {
        if(s.length() == 0){
            if(p.length() == 0) return true;
            else{
                for(int i = 0; i < p.length(); i++){
                    if(p.charAt(i) != '*') return false;
                }
                return true;
            }
        }
        if(p.length() == 0 ) return false;
        boolean[][] dp = new boolean[s.length()+1][p.length()+1];
        dp[0][0] = true;
        for( int i = 0 ;i < p.length() && dp[0][i] && p.charAt(i) =='*'; i++)
            dp[0][i+1] = true;

        for(int i = 0; i < s.length(); i++){
            for(int j = 0; j < p.length(); j++){
                if(dp[i][j] && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '?'))
                    dp[i+1][j+1] = true;
                if(p.charAt(j) == '*'){
                    if(dp[i][j] || dp[i+1][j] || dp[i][j+1]) dp[i+1][j+1] = true;
                }
            }
        }
        return dp[s.length()][p.length()];
    }
}

public class Solution {
    public boolean isMatch(String s, String p) {
        
        
        char[] S = s.toCharArray();
        char[] P = p.toCharArray();
        
        int checkpointS = -1;
        int checkpointP = -1;
        
        int j = 0;
        
        for(int i = 0; i < S.length; /*void*/){
            
            if(j < P.length) {

                if(S[i] == P[j] || P[j] == '?'){
                    i++;
                    j++;
                    continue;
                }   
                
                if(P[j] == '*'){
                    
                    checkpointS = i;
                    checkpointP = j;
                    
                    j++;
                    continue;
                }
            }
            
            // mismatch
            
            if(checkpointS >= 0){
                
                checkpointS++;
                
                // restore
                i = checkpointS;
                j = checkpointP + 1;
                continue;
            }
            
            return false;
        }
        
        while(j < P.length) {
            if(P[j] == '*'){
                j++;
            } else {
                return false;
            }
        }
        
        return true;
    }
}