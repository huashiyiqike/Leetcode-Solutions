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
    public void helper(TreeNode cur, String path, List<String> res){
        String newpath = path + cur.val + "->";
        if(cur.left == null && cur.right == null){
            res.add(newpath.substring(0, newpath.length()-2));
        }
        else{
            if(cur.left != null)
                helper(cur.left, newpath, res);
            if(cur.right != null)
                helper(cur.right, newpath, res);
        }
    }
    public List<String> binaryTreePaths(TreeNode root) {
        if(root == null) return new LinkedList<>();
        List<String> res = new LinkedList<>();
        helper(root, "", res);
        return res;
    }
}