import java.util.*;
public class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length() != t.length()) return false;
        Set<Character> set = new HashSet<>();
        Map<Character, Character> map = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            if(map.get(s.charAt(i)) != null){
                if(map.get(s.charAt(i)) != t.charAt(i)){
                    return false;
                }
            }else{
                if(set.contains(t.charAt(i))) return false;
                map.put(s.charAt(i), t.charAt(i));
                set.add(t.charAt(i));
            }
        }
        return true;
    }
}

public class Solution {

    boolean isIsomorphic(char[] S, char[] T) {
        char[] MAP = new char[256];

        for(int i = 0; i < S.length; i++) {

            if(MAP[(int)S[i]] == 0) {
                // not mapped
                MAP[(int)S[i]] = T[i];
            } else {

                if ( MAP[(int)S[i]] != T[i]) {
                    return false;
                }
            }

        }

        return true;
    }

    public boolean isIsomorphic(String s, String t) {

        char[] S = s.toCharArray();
        char[] T = t.toCharArray();

        if(S.length != T.length) return false;

        return isIsomorphic(S, T) && isIsomorphic(T, S);

    }
}
