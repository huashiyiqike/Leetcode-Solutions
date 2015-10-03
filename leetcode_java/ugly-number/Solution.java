public class Solution {
    public int helper(int num, int div){
        while(num % div == 0 && num >= div) num /= div;
        return num;
    }
    public boolean isUgly(int num) {
        num = helper(num, 2);
        num = helper(num, 3);
        num = helper(num, 5);
        return num == 1;
    }
}