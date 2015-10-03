import java.util.*;

public class Solution {
    public boolean isValid(String s){
        if(s.equals("0") ||(s.charAt(0) != '0' &&Long.parseLong(s)<256)) return true;
        return false;
    }
    public List<String> restoreIpAddresses(String s) {
        List<String> res = new ArrayList<String>();
        if(s.length()>12) return res;
        for(int i = 1; i < 5;i++){
            for(int j = i+1; j < i+4; j++){
                for(int k = j+1; k < j+4; k++){
                    if(k >= s.length()) break;
                    String s0 = s.substring(0, i), s1 = s.substring(i, j), s2 = s.substring(j, k),
                            s3 = s.substring(k, s.length());
                    if(isValid(s0) && isValid(s1) && isValid(s2)
                            && isValid(s3))
                        res.add(s0+"."+s1+"."+s2+"."+s3);
                }
            }
        }
        return  res;
    }
}
public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> res = new ArrayList<String>();
        int len = s.length();
        for(int i = 1; i<4 && i<len-2; i++){
            for(int j = i+1; j<i+4 && j<len-1; j++){
                for(int k = j+1; k<j+4 && k<len; k++){
                    String s1 = s.substring(0,i), s2 = s.substring(i,j), s3 = s.substring(j,k), s4 = s.substring(k,len);
                    if(isValid(s1) && isValid(s2) && isValid(s3) && isValid(s4)){
                        res.add(s1+"."+s2+"."+s3+"."+s4);
                    }
                }
            }
        }
        return res;
    }
    public boolean isValid(String s){
        if(s.length()>3 || s.length()==0 || (s.charAt(0)=='0' && s.length()>1) || Integer.parseInt(s)>255)
            return false;
        return true;
    }
}
public class Solution {

    static List<String> restoreIpAddresses(String s) {
        List<String> ans = new ArrayList<String>();
        int len = s.length();
        for (int i = 1; i <=3; ++i){  // first cut
            if (len-i > 9) continue;
            for (int j = i+1; j<=i+3; ++j){  //second cut
                if (len-j > 6) continue;
                for (int k = j+1; k<=j+3 && k<len; ++k){  // third cut
                    int a,b,c,d;                // the four int's seperated by "."
                    a = Integer.parseInt(s.substring(0,i));
                    b = Integer.parseInt(s.substring(i,j)); // notice that "01" can be parsed into 1. Need to deal with that later.
                    c = Integer.parseInt(s.substring(j,k));
                    d = Integer.parseInt(s.substring(k));
                    if (a>255 || b>255 || c>255 || d>255) continue;
                    String ip = a+"."+b+"."+c+"."+d;
                    if (ip.length()<len+3) continue;  // this is to reject those int's parsed from "01" or "00"-like substrings
                    ans.add(ip);
                }
            }
        }
        return ans;
    }
}

public class Solution {
    
    ArrayList<String> collect;
    
    String[] stack;
    
    void findnum(String s, int p, int pstack){
        
        if(pstack == 4){
            
            if(p >= s.length()){
                String ip = String.join(".", stack);
                
                collect.add(ip);
            }
            
            return;
        }
        
        for(int i = 1; i <= 3; i++){
            
            if( p + i > s.length())
                return;
            
            String number = s.substring(p, p + i);
            
            if(i > 1 && s.charAt(p) == '0') continue;
            
            if(Integer.parseInt(number) <= 255){
                stack[pstack] = number;
                findnum(s, p + i, pstack + 1);
            } 
            
        }
    }
    
    public List<String> restoreIpAddresses(String s) {
        
        collect = new ArrayList<String>();
        stack = new String[4];
        
        findnum(s, 0 , 0);
        
        return collect;
    }
}
