import java.lang.Integer;
import java.lang.Math;
import java.util.Arrays;

public class Solution {
    public int maximumGap(int[] nums) {
        if (nums.length < 2) return 0;
        int maximum = Integer.MIN_VALUE, minimum = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            maximum = Math.max(maximum, nums[i]);
            minimum = Math.min(minimum, nums[i]);
        }
        int gap = (maximum - minimum) / (nums.length - 1) + 1;
        int[] bucketsmax = new int[nums.length - 1];
        int[] bucketsmin = new int[nums.length - 1];
        Arrays.fill(bucketsmax, Integer.MIN_VALUE);
        Arrays.fill(bucketsmin, Integer.MAX_VALUE);
        for (int i : nums) {
            int idx = (i - minimum) / gap;
            bucketsmax[idx] = Math.max(bucketsmax[idx], i);
            bucketsmin[idx] = Math.min(bucketsmin[idx], i);
        }
        int res = Integer.MIN_VALUE;
        for (int i = 0; i < bucketsmax.length; i++) {
            if (bucketsmin[i] != Integer.MAX_VALUE
                    && bucketsmax[i] == Integer.MIN_VALUE)
                res = Math.max(res, bucketsmax[i] - bucketsmin[i]);
            if (i > 0 && bucketsmin[i] != Integer.MAX_VALUE
                    && bucketsmax[i-1] != Integer.MIN_VALUE)
                res = Math.max(res, bucketsmin[i] - bucketsmax[i - 1]);
        }
        return res;
    }
}

public class Solution {

    static class Bucket {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        void add(int n) {
            min = Math.min(n, min);
            max = Math.max(n, max);
        }
    }

    public int maximumGap(int[] num) {
        if (num.length < 2) return 0;

        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < num.length; i++) {
            max = Math.max(max, num[i]);
            min = Math.min(min, num[i]);
        }


        int gap = (int) Math.ceil((double) (max - min) / (num.length - 1));
        int n = (max - min) / gap + 1;

        Bucket[] buckets = new Bucket[n];

        for (int i = 0; i < num.length; i++) {
            int index = (num[i] - min) / gap;

            if (buckets[index] == null) buckets[index] = new Bucket();

            buckets[index].add(num[i]);
        }

        int maxGap = Integer.MIN_VALUE;

        int prev = min;

        for (int i = 0; i < buckets.length; i++) {
            if (buckets[i] == null) continue;

            maxGap = Math.max(maxGap, buckets[i].min - prev);

            prev = buckets[i].max;
        }

        return maxGap;
    }
}
