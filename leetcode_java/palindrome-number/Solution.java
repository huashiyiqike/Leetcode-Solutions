public class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;
        long newx = 0, oldx = x;
        while(x>0){
            newx *= 10;
            newx += x%10;
            x /= 10;
        }
        return newx == oldx;
    }

    // for overflow
    public boolean isPalindrome2(int x) {

        if (x < 0) return false;

        int p = x;
        int q = 0;

        while (p >= 10){
            q *=10;
            q += p%10;
            p /=10;
        }

        return q == x / 10 && p == x % 10;
    }
}

public class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int temp =x;
        int result = 0;
        while(x>0){
            if(result > (Integer.MAX_VALUE-x%10)/10){
                return false;
            }
            result=result*10+x%10;
            x=x/10;
        }
        if(temp==result){
            return true;
        }
        return false;
    }
}




public class Solution {
    
    int len(int x){
        return (int) Math.log10(x) + 1;
    }
    
    int charAt(int x, int i){
        return (int) (x / Math.pow(10, i)) % 10;
    }
    
    public boolean isPalindrome(int x) {
        if (x < 0 ) return false;
        if (x == 0) return true;
        
        int l = len(x);
        
        for(int i = 0; i < l / 2; i++){
            if(charAt(x, i) != charAt(x, l - i - 1)){
                return false;
            }
        }
        
        return true;
    }
}
