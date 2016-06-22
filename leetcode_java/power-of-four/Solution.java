public class Solution {
    public boolean isPowerOfFour(int num) {
         if(num==0){
            return false;
        }
        while(num%4==0){
           // System.out.println(num);
            num=num/4;
        }
        //System.out.println(num);
        if(num!=1){
            return false;
        }else{
            return true;
        }
    }
}