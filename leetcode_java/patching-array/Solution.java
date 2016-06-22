public class Solution {
    public int minPatches(int[] nums, int n) {
        int len = nums.length;
        long reach = 0;
        int count = 0;
        int index = 0;
        while(reach < n){
            if(index < len && nums[index]<=reach+1){
                reach+=nums[index++];
            }else{
                count++;
                reach=reach*2+1;
            }
        }
        return count;
    }
}