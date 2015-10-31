import java.util.*;

import java.math.BigInteger;

public class Solution {
    public String addBinary(String a, String b) {
        return (new BigInteger(a, 2)).add(new BigInteger(b, 2)).toString(2);
    }
}

public class Solution {
    public String addBinary(String a, String b) {
        List<Integer> p  = new ArrayList<>(), q = new ArrayList<>(),
                res = new ArrayList<>();
        for(Character i: a.toCharArray()){
            p.add((int)i - (int)'0');
        }
        for(Character i: b.toCharArray()){
            q.add((int)i - (int)'0');
        }
        Collections.reverse(p);
        Collections.reverse(q);
        int idx = 0, idy = 0, carry = 0;
        while(idx < p.size() && idy < q.size()){
            int tmpint = p.get(idx) + q.get(idy) + carry;
            res.add(tmpint%2);
            carry = tmpint/2;
            idx++;
            idy++;
        }
        while(idx < p.size() ){
            int tmpint = p.get(idx) + carry;
            res.add(tmpint%2);
            carry = tmpint/2;
            idx++;
        }while(idy < q.size()){
            int tmpint = q.get(idy) + carry;
            res.add(tmpint%2);
            carry = tmpint/2;
            idy++;
        }
        if(carry != 0)
            res.add(1);
        Collections.reverse(res);
        String resstr = "";
        for(Integer i:res) resstr += i;
        return resstr;
    }
}

public class Solution {
    
    int toint(char c){
        if(c >= '0') return c - '0';
        return 0;
    }
    
    int toint(char[] chars, int index){
        if(index < chars.length  && index >=0 ) return toint(chars[index]);
        return 0;
    }
    
    public String addBinary(String a, String b) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        if(a == null || b == null) return null;
        
        char[] ca = a.toCharArray();
        char[] cb = b.toCharArray();
    
        int n = Math.max(ca.length, cb.length);

        int[] s = new int[n + 1];
        
        
        //ca = Arrays.copyOf(ca , n);
        //cb = Arrays.copyOf(cb , n);
        
        for(int i = 0 ; i<n ; i++){
            
            s[i] += toint(ca, ca.length - 1 - i) + toint(cb, cb.length - 1 - i);
            s[i + 1] += s[i] / 2;
            s[i] %= 2;
        }
        
        String ss = "";
        
        for(int i = n - 1; i>=0; i--){
            ss =  ss + s[i];
        }
        
        if ( s[n] == 1 ) ss = "1" + ss;
        
        return ss;
        
    }
}