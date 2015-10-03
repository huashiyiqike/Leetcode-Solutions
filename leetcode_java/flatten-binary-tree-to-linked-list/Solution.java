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
    public TreeNode helper(TreeNode root, TreeNode pre){
        pre.right = root;
        TreeNode tmp = root.right;
        if(root.left != null) pre = helper(root.left, root);
        else pre = root;
        if(tmp != null) pre = helper(tmp, pre);
        root.left = null;
        return pre;
    }
    public void flatten(TreeNode root) {
        if(root == null) return;
        TreeNode pre = new TreeNode(0);
        helper(root, pre);
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
    
   TreeNode prev;

    void preorder(TreeNode root){
        
        if(root == null) return;
        
        TreeNode left  = root.left;
        TreeNode right = root.right;
        
        // root
        if(prev != null){
            prev.right = root;
            prev.left = null;
        }
        
        prev = root;
        
        preorder(left);
        preorder(right);
    }
    

    public void flatten(TreeNode root) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        prev = null;
        preorder(root);
    }
}