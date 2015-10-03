
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
    public List<TreeNode> helper(int start, int end){
        if(start > end) return new ArrayList<TreeNode>(Collections.<TreeNode>singletonList(null));
        List<TreeNode> res = new ArrayList<TreeNode>();
        for(int i = start; i <= end; i++) {
            List<TreeNode> left = helper(start, i-1);
            List<TreeNode> right = helper(i+1, end);
            for(TreeNode l:left){
                for(TreeNode r:right){
                    TreeNode root = new TreeNode(i);
                    root.left = l;
                    root.right = r;
                    res.add(root);
                }
            }

        }
        //System.out.println(start+" "+end+" "+res);
        return res;
    }
    public List<TreeNode> generateTrees(int n) {
        return helper(1, n);
    }
}
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; left = null; right = null; }
 * }
 */
public class Solution {
    
    ArrayList<TreeNode> generateTrees(int[] array){
        if (array.length == 0) return new ArrayList<TreeNode>(Collections.<TreeNode>singletonList(null));
        
        ArrayList<TreeNode> found = new ArrayList<TreeNode>();
        
        for(int i = 0; i < array.length; i++){
            
            for(TreeNode left : generateTrees(Arrays.copyOfRange(array, 0, i))){
                for(TreeNode right : generateTrees(Arrays.copyOfRange(array, i + 1, array.length))){
                    TreeNode root = new TreeNode(array[i]);
                    
                    root.left = left;
                    root.right = right;
                    
                    found.add(root);
                }
            }
        }
        
        return found;
    }
    
    public List<TreeNode> generateTrees(int n) {
                
        int[] array = new int[n];
        
        for(int i = 0; i < n ; i++) array[i] = i + 1;
        
        return generateTrees(array);
    }
}
