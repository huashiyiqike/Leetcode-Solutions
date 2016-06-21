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