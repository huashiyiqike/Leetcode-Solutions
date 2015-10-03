import java.util.*;
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int start = 0, res = 0;
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(map.containsKey(c) && map.get(c)+1 > start) {
                start = map.get(c) + 1;
            }
            map.put(c, i);
            res = Math.max(res, i-start+1);
        }
        return res;
    }
}

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if(s == null) return 0;
        char[] str = s.toCharArray();
        if(str.length == 0) return 0;
        

        int max = 1;
        
        int barrier = 0;

        for(int i = 1; i < str.length; i++){
            for(int j = i - 1; j >= barrier;j--){
                if(str[i] == str[j]){
                    barrier = j + 1;
                    break;
                }
            }
            
            max = Math.max(max, i - barrier + 1);
        }
        
        
        return max;
        
    }
}