import java.util.*;
public class Solution {
    public String reduce(String s){
        int i = 0;
        for(; i < s.length(); i++){
            if(s.charAt(i) != '0') break;
        }
        if(i == s.length()) return "0";
        return s.substring(i, s.length());
    }
    public int compareVersion(String version1, String version2) {
        List<String> v1 = Arrays.asList(version1.split("\\.")),
                v2 = Arrays.asList(version2.split("\\."));
        for(int i = 0; i < v1.size() && i < v2.size(); i++){
            int a = Integer.parseInt(v1.get(i)), b = Integer.parseInt(v2.get(i));
            if(a != b) return a > b?1:-1;
        }

        if(v1.size() == v2.size()) return 0;
        if(v1.size() > v2.size()){
            for(int j = v2.size(); j < v1.size();j++){
                if(Integer.parseInt(v1.get(j)) != 0) return 1;
            }
        }
        else{
            for(int j = v1.size(); j < v2.size();j++){
                if(Integer.parseInt(v2.get(j)) != 0) return -1;
            }
        }
        return 0;
    }
}

public class Solution {
    
    String padding(String s, int len){
        if(s == null) s = "";
        
        char[] p = new char[len - s.length()];
        
        Arrays.fill(p, '0');
        
        return new String(p) + s;
    }
    
    int len(String s){
        if(s == null) return 0;
        return s.length();
    }
    
    public int compareVersion(String version1, String version2) {
        String[] v1 = version1.split("\\.");
        String[] v2 = version2.split("\\.");
        
        int m = Math.max(v1.length, v2.length);
        
        v1 = Arrays.copyOf(v1, m);
        v2 = Arrays.copyOf(v2, m);
        
        for(int i = 0; i < m; i++){
            String s1 = v1[i];
            String s2 = v2[i];
            
            int l = Math.max(len(s1), len(s2));
            
            s1 = padding(s1, l);
            s2 = padding(s2, l);
            
            for(int j = 0; j < l; j++){
                if(s1.charAt(j) > s2.charAt(j)){
                    return 1;
                }else if(s1.charAt(j) < s2.charAt(j)){
                    return -1;
                }
            }
            
        }
        
        return 0;
    }
}
