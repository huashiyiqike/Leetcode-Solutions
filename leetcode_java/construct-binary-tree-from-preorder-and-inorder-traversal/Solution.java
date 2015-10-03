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
    int[] preorder, inorder;
    public TreeNode helper(int startpre, int endpre, int startin, int endin){
        if(startpre > endpre) return null;

        TreeNode root = new TreeNode(preorder[startpre]);

        int i = startin;
        for(; i <= endin; i++){
            if(inorder[i] == preorder[startpre]) break;
        }
        root.left = helper(startpre+1, startpre+i-startin, startin, i-1);
        root.right = helper(endpre-endin+i+1, endpre, i+1, endin);

        return root;
    }
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        return helper(0, preorder.length-1, 0, inorder.length-1);
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
    
    int p = 0;
    int[] preorder;
    int[] inorder;
    
    
    TreeNode buildTree(int st, int ed){
        
        if(st >= ed) return null; //
        
        TreeNode root = new TreeNode(preorder[p]);
        
        int i;
        for(i = st ; i< ed && inorder[i] != preorder[p] ; i++);

        p++;
        root.left = buildTree(st, i);
        root.right = buildTree(i + 1, ed);
        
        return root;
    }
    
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // Note: The Solution object is instantiated only once and is reused by each test case.

        this.preorder = preorder;
        this.inorder = inorder;
        this.p = 0;
        //if (preorder.length == 0) return null;
        return buildTree(0 , inorder.length);
        //return new TreeNode(preorder[p]);
    }
}