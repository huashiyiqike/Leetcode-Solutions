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
    TreeNode first = null, second = null, pre = null;
     //first larger than follow, second smaller than pre
    public void helper(TreeNode root){
        if(root.left != null) helper(root.left);
        if(pre != null && root.val < pre.val){
            if(first == null)
                first = pre;
            second = root;
        }
        pre = root;
        if(root.right != null) helper(root.right);
    }
    public void recoverTree(TreeNode root) {
        helper(root);
        int tmp = first.val;
        first.val = second.val;
        second.val = tmp;
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
    
    TreeNode[] bad;
    TreeNode last;
    
    
    void inorder(TreeNode root){
        
        if(root.left != null) inorder(root.left);
        
        if(last != null && last.val > root.val){ //
            bad[0] = root;
            
            if(bad[1] == null) bad[1] = last;
        }
        
        last = root;
        
        
        if(root.right != null) inorder(root.right);
        
    }
    
    public void recoverTree(TreeNode root) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if(root == null) return;
        
        bad = new TreeNode[2];
        bad[0] = null;
        bad[1] = null;
        last = null;

        inorder(root);
        

        if(bad[0] != null && bad[1] != null){
            int t = bad[0].val;
            bad[0].val = bad[1].val;
            bad[1].val = t;          
        }
        
        
    }
}