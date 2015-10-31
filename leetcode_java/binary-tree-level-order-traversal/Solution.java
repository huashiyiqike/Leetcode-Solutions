import java.util.*;
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<Integer> tmpres = new ArrayList<Integer>();
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Deque<TreeNode> queue = new LinkedList<TreeNode>(),
                next = new LinkedList<TreeNode>();
        if(root != null) queue.offer(root);
        while(!queue.isEmpty()){
            tmpres.clear();
            next.clear();
            while(!queue.isEmpty()) {
                TreeNode cur = queue.poll();
                if (cur.left != null) next.offer(cur.left);
                if (cur.right != null) next.offer(cur.right);
                tmpres.add(cur.val);
            }
            res.add(new LinkedList<Integer>(tmpres));
            queue = new LinkedList<TreeNode>(next);
        }
        return res;
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        ArrayList<List<Integer>> rt = new  ArrayList<List<Integer>>();
        
        if(root == null) return rt;
        
        final TreeNode END = new TreeNode(0);
        
        Deque<TreeNode> queue = new LinkedList<TreeNode>();
        
        queue.add(root);
        queue.add(END);
        
        ArrayList<Integer> level = new ArrayList<Integer>();
        
        while(!queue.isEmpty()){
            
            TreeNode node = queue.poll();
            
            if(node == END){
                rt.add(new ArrayList<Integer>(level)); // copy
                level.clear();
                
                if(!queue.isEmpty()) queue.add(END);
                
            }else{
                
                level.add(node.val);
                                
                if(node.left != null)  queue.addLast(node.left);
                if(node.right != null) queue.addLast(node.right);
            }
        }
        
        return rt;
        
    }
}
