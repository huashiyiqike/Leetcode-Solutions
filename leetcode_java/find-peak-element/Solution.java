public class Solution {
    public int helper(int[] nums, int l, int r){
        if(l == r) return l;
        int mid = (l+r)/2;
        int idx1 = helper(nums, l, mid), idx2 = helper(nums, mid+1, r);
        return nums[idx1] > nums[idx2]?idx1:idx2;
    }
    public int findPeakElement(int[] nums) {
        return helper(nums, 0, nums.length - 1);
    }
}

public class Solution {

    int findPeakElement(int[] num, int from, int to) {
        if (to - from == 1) return from;

        int m = (to + from) / 2;

        int l = findPeakElement(num, from, m);
        int r = findPeakElement(num, m, to);

        if (num[l] > num[r]) return l;
        else return r;
    }

    public int findPeakElement(int[] num) {
        return findPeakElement(num, 0, num.length);
    }
}
