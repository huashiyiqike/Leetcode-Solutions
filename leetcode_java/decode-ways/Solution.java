public class Solution {
    public int numDecodings(String s) {
        if(s.length()==0 || s.charAt(0) == '0') return 0;
        int[] dp = new int[s.length()+1];
        dp[s.length()] = 1;
        for(int i = s.length()-1; i >= 0; i--){
            if(s.charAt(i) == '0'){
                dp[i] = 0;
            }else{
                dp[i] = dp[i+1];
            }
            if(i < s.length()-1 && (
                    s.charAt(i) == '1' || (s.charAt(i) == '2' && s.charAt(i+1) <'7')
                    ))
                dp[i] = dp[i+1] + dp[i+2];
        }
        return dp[0];
    }
}

public class Solution {
    
    public int numDecodings(String s) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.

        final char[] _s = s.toCharArray();
        final int n = _s.length;
        
        if (n == 0 ) return 0;
        
        int[] step = new int[Math.max(n + 1, 3)];
        
        step[0] = 1;
        
        step[1] = 0;
        
        if(_s[0] != '0')
            step[1] = 1;

        for(int i = 2; i <= n; i++){
            
            step[i] = 0;
            
            if ( _s[i - 1] != '0' ){
                step[i] += step[i - 1];
            }
            
            if ( _s[i - 2] != '0' ){
                if ( (_s[i - 2] - '0') * 10 + (_s[i - 1] - '0') <= 26 )
                    step[i] += step[i - 2];
            }
            
        }
        
        return step[n];
    }

}