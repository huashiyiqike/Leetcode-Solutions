public class Solution {
    public int findDuplicate(int[] nums) {
        int left = 1, right = nums.length;
        while(left <= right){
            int mid = (left + right) / 2;
            int count = 0;
            for(int tmp:nums){
                if(tmp <= mid) count++;
            }
            if(count <= mid) left = mid+1;
            else if(count > mid) right = mid - 1;
        }
        return left;
    }
}