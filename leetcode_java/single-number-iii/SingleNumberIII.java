public class Solution {
    public int[] singleNumber(int[] nums) {
        int len = nums.length;
        int res = 0;
        for(int i = 0;i < len ; i++){
            res = (res^nums[i]);
        }
        int first_diff_bit = 0;
        for(int i = 0;i < 32;i++){
            if(((res >> i) &1) == 1){
                first_diff_bit=i;
                break;
            }
        }
        int first = 0;
        for(int i = 0; i < len ; i++){
            if(((nums[i] >> first_diff_bit) & 1) == 1){
                first = (first ^ nums[i]);
            }
        }
        int[] result = new int[2];
        result[0] = first;
        result[1] = first ^ res;
       return result;
    }
}