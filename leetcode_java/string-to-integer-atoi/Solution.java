public class Solution {
    public int myAtoi(String str) {
        if(str == null || str.length() == 0){
            return 0;
        }
        str = str.trim();
        int len = str.length();
        double sum = 0;
        int flag = 1;
        int index = 0;
        if(str.charAt(index) == '-'){
           flag = -1;
           index++;
        }else if(str.charAt(index) == '+'){
           index++;
        }
         while(index < len &&(str.charAt(index) >= '0' && str.charAt(index) <= '9')){
            sum =sum * 10 + (str.charAt(index)-'0');
            index ++ ;
        }
        sum = sum * flag;
        if(sum > Integer.MAX_VALUE){
            sum = Integer.MAX_VALUE;
        }else if(sum < Integer.MIN_VALUE){
           sum = Integer.MIN_VALUE;
        }
        
        return (int)(sum);
    }
}

import java.math.BigInteger;

public class Solution {
    public int myAtoi(String str) {
        str = str.trim();
        char[] chars = str.toCharArray();
        boolean neg = false;
        int idx = 0;
        while(idx < chars.length && (chars[idx] == ' ')) idx++;
        BigInteger res = BigInteger.ZERO;
        if(idx < chars.length && (chars[idx] == '-' || chars[idx] == '+')){
            if( chars[idx] == '-')
                neg = true;
            idx++;
        }
        for(int i = idx ; i < chars.length && chars[i] <= '9' && chars[i] >= '0'; i++){
            res = res.multiply(BigInteger.valueOf(10));
            res = res.add(BigInteger.valueOf((int)chars[i] - (int)'0'));
        }
        if(neg) res = res.multiply(BigInteger.valueOf(-1));
        if(res.compareTo(BigInteger.valueOf(Integer.MAX_VALUE)) == 1)
            res = BigInteger.valueOf(Integer.MAX_VALUE);
        if(res.compareTo(BigInteger.valueOf(Integer.MIN_VALUE)) == -1)
            res = BigInteger.valueOf(Integer.MIN_VALUE);
        return res.intValue();
    }
}

public class Solution {
    public int atoi(String str) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        
        // null "" 
        if (str == null || "".equals(str))
            return 0;
        
        char[] ds = str.toCharArray();
        
        int sum = 0;
        
        int sign = 1;
        
        int s = 0;
        
        boolean signseen = false;
        
        while(s < ds.length && !('0' <= ds[s] && ds[s] <= '9')){
            
            if(signseen)
                return 0;
                
            
            
            if(ds[s] == '-'){
                sign *= -1;
                signseen = true;
            }else if(ds[s] == '+'){
                signseen = true;
            }else if(ds[s] != ' '){
                return 0;
            }
            
            s++;
        }
        
        int e = s;
        while(e < ds.length && ('0' <= ds[e] && ds[e] <= '9')){
            e++;
        }
        
        int p = 0;
        
        boolean flago = false;
        for(int i  = s; i < e ; i++){

            if(sum > Integer.MAX_VALUE / 10 || (sum == Integer.MAX_VALUE / 10 && ds[i] - '0' > Integer.MAX_VALUE % 10 ))
                flago = true;
                
            sum = sum * 10 + (ds[i] - '0');
        }
        
        if (flago)
            if(sign > 0)
                return Integer.MAX_VALUE;
            else
                return Integer.MIN_VALUE;
                
        return sum * sign;
        
    }
}