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
    public int countNodes(TreeNode root) {
        if(root == null) return 0;
        int left_h = 0, right_h = 0;
        TreeNode tmp = root;
        while(tmp.left!= null){
            left_h++;
            tmp = tmp.left;
        }
        tmp = root;
        while(tmp.right != null){
            right_h++;
            tmp = tmp.right;
        }
        if(left_h == right_h) return (2<<left_h) - 1;
        return 1 + countNodes(root.left) + countNodes(root.right);
    }
}
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
    
    int height(TreeNode root){
        if(root == null) return 0;
        
        return 1 + height(root.left);
    }
    
    
    int leaves = 0;
    boolean stop = false;
    
    void countLeaves(TreeNode root, int heightToLeaf){
        
        if(root == null) return;
        
        if(stop) return;
        
        if(heightToLeaf == 2) {

            if(root.right != null){
                leaves += 2;
            } else {
                
                // at lease one is null
                stop = true;
                
                if(root.left  != null) { 
                    leaves += 1;
                }
            }
            
            
            return;
        }
        
        countLeaves(root.left,  heightToLeaf - 1);
        countLeaves(root.right, heightToLeaf - 1);
    }
    
    int perfectTreeNodeCount(int height){
        if(height == 0) return 0;
        if(height == 1) return 1;
        
        return (int)Math.pow(2, height) - 1;
    }
    
    public int countNodes(TreeNode root) {
        
        int h = height(root);

        countLeaves(root, h);
        
        if(!stop){
            // perfect tree
            return perfectTreeNodeCount(h);
        }
        
        return perfectTreeNodeCount(h - 1) + leaves;
    }
}
