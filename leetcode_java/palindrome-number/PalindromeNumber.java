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