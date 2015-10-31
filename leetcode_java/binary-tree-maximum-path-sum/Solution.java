/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    int sum = Integer.MIN_VALUE;

    public int helper(TreeNode root) {
        if (root == null) return 0;
        int left = Math.max(0, helper(root.left));
        int right = Math.max(0, helper(root.right));
        sum = Math.max(sum, left + right + root.val);
        return Math.max(left, right) + root.val;
    }

    public int maxPathSum(TreeNode root) {
        helper(root);
        return sum;
    }
}

public class Solution {
    public int[] helper(TreeNode root) {
        if (root == null) return new int[]{0, Integer.MIN_VALUE};
        int[] left = helper(root.left);
        int[] right = helper(root.right);
        int[] res = {Math.max(0, Math.max(left[0], right[0]) + root.val),
                Math.max(left[1], Math.max(right[1], left[0] + right[0] + root.val))};
        return res;
    }

    public int maxPathSum(TreeNode root) {
        if (root == null) return 0;
        return helper(root)[1];
    }
}

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {

    int max;

    int sum(TreeNode root) {
        if (root == null) return 0;

        int left = sum(root.left);
        int right = sum(root.right);

        left = Math.max(left, 0);
        right = Math.max(right, 0);

        int sum = root.val + left + right;
        max = Math.max(max, sum);

        return Math.max(left, right) + root.val;
    }

    public int maxPathSum(TreeNode root) {

        max = Integer.MIN_VALUE;
        sum(root);

        return max;
    }
}