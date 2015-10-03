public class Solution {
    public double myPow(double x, int n) {
        boolean neg = false;
        if(n < 0) {
            neg = true;
            n = -n;
        }
        double res = 1;
        while(n > 0){
            if((n & 1) == 1) res *= x;
            n >>= 1;
            x *= x;
        }
        if(neg) return 1.0/res;
        return res;
    }
}

public class Solution {
    public double myPow(double x, int n) {
        
        if(n == 0) return 1;
        
        double s = myPow(x, n / 2);
        
        if(n % 2 == 0) return s * s;
        
        if(n > 0) return s * s * x;
        // else n < 0
        return s * s / x;
    }
}
