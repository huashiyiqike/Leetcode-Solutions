public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        boolean[] dp = new boolean[s.length()+1];
        dp[0] = true;
        for(int i = 0; i < s.length(); i++){
            for(int j = i+1; j <= s.length(); j++){
                if(dp[i] && wordDict.contains(s.substring(i,j)))
                    dp[j] = true;
            }
        }
        return dp[dp.length-1];
    }
}
// TLE
//public class Solution {
//    public boolean wordBreak(String s, Set<String> wordDict) {
//        if(s.length() == 0) return true;
//        boolean res = false;
//        for(int i = 1; i < s.length; i++){
//            if(wordDict.contains(s.substring(0,i)))
//                res |= wordBreak(s.substring(i,s.length()), wordDict);
//        }
//        return res;
//    }
//}
public class Solution {
    public boolean wordBreak(String s, Set<String> dict) {
        
        char[] S = s.toCharArray();
        
        boolean[] P = new boolean[S.length + 1];
        P[0] = true;
        
        for(int i = 0; i < S.length; i++){
            
            for(int j = 0; j <= i; j++){
                if(P[j] && dict.contains(new String(S, j, i - j + 1))){
                    P[i + 1] = true;
                    continue;
                }
            }
        }
        
        return P[S.length];
        
        
    }
}