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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Deque<TreeNode> stack = new LinkedList<TreeNode>();
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
        while (!stack.isEmpty()) {
            TreeNode cur = stack.poll();
            res.add(cur.val);
            if (cur.right != null) {
                cur = cur.right;
                while (cur != null) {
                    stack.push(cur);
                    cur = cur.left;
                }
            }
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
    
    static enum ReturnAddress {
        PRE, IN, POST, DONE;
    }
    
    static class StackState {
        ReturnAddress returnAddress = ReturnAddress.PRE;
        TreeNode param;
        
        StackState(TreeNode param){
            this.param = param;
        }
    }
    
    public List<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> rt = new ArrayList<>();

        Deque<StackState> stack = new LinkedList<>();
        
        if(root != null)
            stack.push(new StackState(root));
        
        while(!stack.isEmpty()){
            
            StackState current = stack.pop();
            
            switch(current.returnAddress){
                case PRE:
                    current.returnAddress = ReturnAddress.IN;
                    
                    if(current.param.left != null){
                        stack.push(current);
                        stack.push(new StackState(current.param.left));
                        continue;
                    }
                    
                case IN:
                    current.returnAddress = ReturnAddress.POST;

                    rt.add(current.param.val);
                    
                case POST:
                    current.returnAddress = ReturnAddress.DONE;
                
                    if(current.param.right != null){
                        stack.push(current);
                        stack.push(new StackState(current.param.right));
                        continue;
                    }                
                default:
                    break;
            }
        }
        
        
        return rt;
    }
}
