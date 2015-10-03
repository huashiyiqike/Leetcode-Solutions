import java.util.*;
public class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> dict = new HashMap<>(), has = new HashMap<>();
        for(char i:t.toCharArray()){
            if(dict.containsKey(i)) dict.put(i, dict.get(i)+1);
            else dict.put(i, 1);
            has.put(i, 0);
        }
        int left = 0, right = 0, count = 0, minlen = Integer.MAX_VALUE, lindex = -1, rindex = -1;
        char[] cha = s.toCharArray();
        while(right < s.length()){
            while(right < s.length() && count < t.length()){
                if(dict.get(cha[right]) != null){
                    if(has.get(cha[right]) < dict.get(cha[right])) count++;
                    has.put(cha[right], has.get(cha[right])+1);
                }
                right++;
            }
            while(left < right && count == t.length()){
                if(dict.get(cha[left]) != null){
                    if(has.get(cha[left]).equals(dict.get(cha[left]))) count--;
                    has.put(cha[left], has.get(cha[left])-1);
                    if(right-left < minlen && count == t.length()-1) {
                        minlen = Math.min(minlen, right-left);
                        lindex = left;
                        rindex = right;
                    }
                }
                left++;
            }

        }
        if(lindex >= 0 && rindex >=0)
        return s.substring(lindex, rindex);
        else return "";
    }
}

public class Solution {
    public String minWindow(String S, String T) {
        char[] s = S.toCharArray();
        char[] t = T.toCharArray();
        
        if ( t.length == 0) return "";
        if ( t.length > s.length ) return "";
        
        
        int mstart = 0;
        int mend = -1;
        
        int gstart = 0;
        int gend = 0;
        
        int[] need = new int[256];
        int[] seen = new int[256];
        
        int checksum = 0;
        
        for(char c : t){
            need[(int)c]++;
        }

        for(/*void*/; gend < s.length; gend++ ){
            
            int i = (int)s[gend];
            if(need[i] > 0){
                seen[i]++;
                
                if(seen[i] <= need[i])
                    checksum++;
            }
            
            
            if(checksum == t.length){
                
                if(mend < 0) mend =  s.length - 1;
                
                for(/*void*/; gstart <= gend; gstart++){
                    
                    i = (int)s[gstart];
                    if(need[i] > 0){
                        if( seen[i] > need[i] ){
                            seen[i]--;
                        } else {
                            break;
                        }
                    }
                }
                
                if(gend - gstart < mend - mstart ){
                    mstart = gstart;
                    mend = gend;
                }
                
            }
            
        }


        return S.substring(mstart, mend + 1);
    }
}