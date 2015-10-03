public class Solution {
    public int reverse(int x) {
        int neg = 1;
        if(x<0){
            neg = -1;
            x = -x;
        }
        long res = 0;
        while(x > 0){
            res *= 10;
            res += x%10;
            x /= 10;
        }
        res *= neg;
        if(res < Integer.MIN_VALUE || res > Integer.MAX_VALUE) return 0;
        return (int)res;
    }
}
public class Solution {
    public int reverse(int x) {
        
        if(x == Integer.MIN_VALUE) return 0;
        if(x < 0) return -reverse(-x);
        
        int y = 0;

         do {

            // y * 10 + x % 10 > Integer.MAX_VALUE
            if(y > (Integer.MAX_VALUE - x % 10) / 10){
                return 0;
            }
            
            y = y * 10 + x % 10;
            
            x /= 10;
            
        } while(x > 0);

        return y;
    }
}
