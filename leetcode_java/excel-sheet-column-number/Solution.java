public class Solution {
    public int titleToNumber(String s) {
        char[] nums = s.toCharArray();
        int res = 0;
        for(int i = 0; i < nums.length; i++){
            res *= 26;
            res += (int)nums[i] - (int)'A' + 1;
        }
        return res;
    }
}
public class Solution {
    public int titleToNumber(String s) {
        char[] S = s.toCharArray();
        
        int n = 0;
        
        int p = 1;
        
        for(int i = S.length - 1; i >= 0; i--){
            
            n += (S[i] - 'A' + 1) * p;
            
            p *= 26;    
        }
        
        return n;
    }
}
