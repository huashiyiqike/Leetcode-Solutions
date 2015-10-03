public class Solution {
    public int countDigitOne(int n) {
        // count 1 in every bit
        long res = 0;
        for(int i = 1; i < n ; i *= 10){
            res += (long)n/i + n%(i*10);
        }
        return (int)res;
    }
}
public class Solution {
    public int countDigitOne(int n) {
        // count 1 in every bit
        long res = 0;
        for(int i = 10; i <= n*10 ; i *= 10){
            int tmp = n - (n/i)*i;
            tmp = tmp > (i/10) ? (i/10) : (tmp - i/10);
            tmp = tmp > 0 ? tmp: 0;
//            int tmp = (n%i - i/10 + 1)>(i/10)?(i/10): (n%i - i/10 + 1);
            res += n/i + tmp;
        }
        return (int)res;
    }
}
public class Solution {
    public int countDigitOne(int n) {
        long res = 0;
        int cur = 10, tmp = 1;
        while(n > cur){
            int a = n/cur, b = n % (cur/10);
            res += a*tmp + b;
        }
    }
}