import java.util.*;

public class Solution {
    public String fractionToDecimal(long numerator, long denominator) {
        boolean neg = false;
        if((numerator > 0 && denominator < 0) || (numerator < 0 && denominator > 0))
            neg = true;
        numerator = Math.abs(numerator);
        denominator = Math.abs(denominator);
        String res = "";
        if(neg) res = "-";
        if(denominator == 0) return "0";
        if(numerator % denominator == 0){
            return res + numerator/denominator;
        }

        res += numerator / denominator + ".";
        numerator %= denominator;
        Map<Long, Integer> dict = new HashMap<>();
        dict.put(numerator, res.length());
        while(numerator > 0){
            numerator *= 10;
            res += numerator / denominator;
            numerator %= denominator;
            if(dict.containsKey(numerator)) {
                res = res.substring(0, dict.get(numerator)) + "("
                        + res.substring(dict.get(numerator), res.length()) + ")";
                break;
            }
            else
                dict.put(numerator, res.length());
        }
        return res;
    }
}

public class Solution {
    
    public String fractionToDecimal(int numerator, int denominator) {

        String sign = "";
        
        if(Math.signum(numerator) * Math.signum(denominator) < 0){
            sign = "-";
        }

        // cheat ...
        long _numerator = numerator;
        
        long quotient = _numerator / denominator;
            
        _numerator %= denominator;
        _numerator *= 10;
        
        final String intPart = "" + Math.abs(quotient);
        
        Map<String, Integer> mod = new HashMap<String, Integer>();
        
        int i = 0;
        
        StringBuilder sb = new StringBuilder();
        
        while(_numerator != 0){
            quotient = Math.abs(_numerator / denominator);
            
            _numerator %= denominator;
            
            Integer start = mod.get(_numerator + "," + quotient);
            
            if(start != null){
                sb.insert(start, "(");
                sb.append(")");
                break;
            }
            
            sb.append(quotient);
            
            mod.put(_numerator + "," + quotient, i);
            
            _numerator *= 10;
            i++;
        }
        
        String fractionalPart = sb.toString();

        if(!"".equals(fractionalPart)) fractionalPart = "." + fractionalPart;
        
        return sign + intPart + fractionalPart;
        
    }
}
