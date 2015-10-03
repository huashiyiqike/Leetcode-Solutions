public class Solution {
    public void rotate(int[] nums, int start, int end){
       while(start < end){
           int tmp = nums[start];
           nums[start] = nums[end];
           nums[end] = tmp;
           start++;
           end--;
       }
    }
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        k = nums.length - k;
        rotate(nums, 0, k-1);
        rotate(nums, k, nums.length-1);
        rotate(nums, 0, nums.length-1);
    }
}
public class Solution {
    public void rotate(int[] nums, int k) {
        
        if(k == 0) return;


        int c = 0;

        for(int j = 0; j < k; j++) {
            int i = j;
            int t = nums[i];


            for (;;) {

                i = (i + k) % nums.length;

                int nt = nums[i];

                nums[i] = t;

                t = nt;

                c++;

                if (i == j) break;
            }

            if(c == nums.length) break;
        }
        
    }
}
