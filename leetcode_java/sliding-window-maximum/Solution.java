import java.util.*;
import java.util.LinkedList;

public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0) return nums;
        int length = nums.length - k >= 0 ? nums.length - k + 1 : 1;
        Deque<Integer> queue = new LinkedList<>();
        int[] res = new int[length];
        for (int i = 0; i < nums.length; i++) {
            if (!queue.isEmpty() && queue.peek() <= i - k) queue.poll();
            while (!queue.isEmpty() && nums[queue.getLast()] < nums[i]) {
                queue.pollLast();
            }
            queue.offer(i);
            if (i + 1 >= k) res[i + 1 - k] = nums[queue.peek()];
        }
        return res;
    }
}