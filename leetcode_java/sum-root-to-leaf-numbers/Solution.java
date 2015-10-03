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
    public int helper(TreeNode root, int pre){
        if(root == null) return 0;
        pre = pre * 10 + root.val;
        if(root.left == null && root.right == null) return pre;
        return helper(root.left, pre) + helper(root.right, pre);
    }
    public int sumNumbers(TreeNode root) {
        return helper(root, 0);
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
    
    int sumNumbers(TreeNode root, int parentval){
        
        if(root == null) return 0;
        
        int p = parentval * 10 + root.val;
        
        if(root.left == null && root.right == null) return p;
        
        return sumNumbers(root.left, p) + sumNumbers(root.right, p);
        
    }
    
    public int sumNumbers(TreeNode root) {
        return sumNumbers(root, 0);
    }
}
