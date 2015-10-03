public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int l = 0, r = 0, sum =0, minlen = Integer.MAX_VALUE;
        while(r < nums.length){
            while(r < nums.length && sum < s){
                sum += nums[r];
                r++;
            }
            while(l < r && sum >= s){
                if(sum >= s) minlen = Math.min(minlen, r-l);
                sum -= nums[l];
                l++;
            }

        }
        if(minlen != Integer.MAX_VALUE)
            return minlen;
        else return 0;
    }
}

public class Solution {
    public int minSubArrayLen(int s, int[] nums) {

        int sum = 0;

        int st = 0;

        int c = nums.length + 1;

        for (int i = 0; i < nums.length; i++) {

            sum += nums[i];

            if(sum >= s){
                while(sum - nums[st] >= s) {
                    sum -= nums[st++];
                }

                c = Math.min(c, i - st + 1);
            }

        }

        if(c > nums.length) {
            return 0;
        }

        return c;
    }
}
