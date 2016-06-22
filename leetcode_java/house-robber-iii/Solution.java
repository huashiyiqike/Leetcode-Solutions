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
    int[] arr=new int[2];
    public int rob(TreeNode root) {
        if(root==null){
            return 0;
        }
        return dfs(root)[0];
    }
   public int[] dfs(TreeNode root){
       int[] left=new int[2];
        int[] right=new int[2];
       if(root.left!=null){
            left=dfs(root.left);
       }
       if(root.right!=null){
             right=dfs(root.right);
       }
       
     
       int[] rootNew=new int[2];
       rootNew[1]=left[0]+right[0];
       rootNew[0]=Math.max(left[1]+right[1]+root.val,rootNew[1]);
       return rootNew;
    }
}