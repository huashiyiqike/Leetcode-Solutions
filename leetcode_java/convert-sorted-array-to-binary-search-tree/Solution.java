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
    public TreeNode sortedArrayToBST(int[] num) {
        if (num == null || num.length == 0)
            return null;
        return helper(num, 0, num.length - 1);
    }

    private TreeNode helper(int[] num, int l, int r) {
        if (l > r)
            return null;
        int m = (l + r) / 2;
        TreeNode root = new TreeNode(num[m]);
        root.left = helper(num, l, m - 1);
        root.right = helper(num, m + 1, r);
        return root;
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
    
    //TreeNode
    
    public TreeNode sortedArrayToBST(int[] num) {
        
        if(num.length == 0)
            return null;
        
        if(num.length == 1)
            return new TreeNode(num[0]);
        
        int mid = num.length / 2;
        
        TreeNode root = new TreeNode(num[mid]);
        
        root.left = sortedArrayToBST(Arrays.copyOfRange(num, 0, mid));
        root.right = sortedArrayToBST(Arrays.copyOfRange(num, mid + 1, num.length));
        
        return root;
        
    }
}