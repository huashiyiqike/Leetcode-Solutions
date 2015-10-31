public class Solution {
    public int jump(int[] nums) {
        int maxl = 0;
        int step = 0;
        int cur = 0;
        while (cur < nums.length - 1) {
            int newmaxl = cur + nums[cur];
            for (int i = maxl + 1; i <= cur; i++) {
                newmaxl = Math.max(newmaxl, i + nums[i]);
            }
            maxl = cur;
            cur = newmaxl;
            step++;
        }
        return step;
    }
}

public class Solution {
    public int jump(int[] nums) {
        int maxl = 0;
        int step = 0;
        for (int i = 0; i < nums.length - 1; ) {
            int newmaxl = i + nums[i];
            for (int j = maxl + 1; j <= i; j++) {
                newmaxl = Math.max(newmaxl, j + nums[j]);
            }
            maxl = i;
            i = newmaxl;
            step++;
        }
        return step;
    }
}

public class Solution {
    public int jump(int[] A) {
        int count = 0;
        int laststep = 0;

        for (int i = 0; i < A.length - 1; /**/) {

            int maxstep = i + A[i];
            for (int j = laststep + 1; j <= i; j++) {
                maxstep = Math.max(maxstep, j + A[j]);
            }

            laststep = i;
            i = maxstep;

            count++;
        }

        return count;
    }
}