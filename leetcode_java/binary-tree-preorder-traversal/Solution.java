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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();

        Deque<TreeNode> stack = new LinkedList<TreeNode>();
        if(root == null) return res;
        stack.push(root);
        while(!stack.isEmpty()){
            TreeNode tmp = stack.pop();
            while(tmp != null){
                res.add(tmp.val);
                if(tmp.right != null) stack.push(tmp.right);
                if(tmp.left != null) tmp = tmp.left;
                else break;
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
    
    public List<Integer> preorderTraversal(TreeNode root) {
        
        ArrayList<Integer> rt = new ArrayList<>();

        Deque<StackState> stack = new LinkedList<>();
        
        if(root != null)
            stack.push(new StackState(root));
        
        while(!stack.isEmpty()){
            
            StackState current = stack.pop();
            
            switch(current.returnAddress){
                case PRE:
                    current.returnAddress = ReturnAddress.IN;
                    rt.add(current.param.val);
                    
                case IN:
                    current.returnAddress = ReturnAddress.POST;
                    
                    if(current.param.left != null){
                        stack.push(current);
                        stack.push(new StackState(current.param.left));
                        continue;
                    }
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
