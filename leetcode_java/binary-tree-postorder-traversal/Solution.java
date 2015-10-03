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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Deque<TreeNode> stack = new LinkedList<TreeNode>();
        if(root != null) stack.push(root);
        TreeNode last = new TreeNode(0);
        while(!stack.isEmpty()){
            TreeNode tmp = stack.peek(); // or getFirst(), deque implements push from head
            if(last == tmp.left) {
                if(tmp.right != null) stack.push(tmp.right);
                else res.add(stack.pop().val);
            }
            else if(last == tmp.right || (tmp.left == null && tmp.right == null)){
                res.add(stack.pop().val);
            }
            else{
                if(tmp.right != null) stack.push(tmp.right);
                if(tmp.left != null) stack.push(tmp.left);
            }
            last = tmp;
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
    
    public List<Integer> postorderTraversal(TreeNode root) {
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
                
                    if(current.param.right != null){
                        stack.push(current);
                        stack.push(new StackState(current.param.right));
                        continue;
                    }

                case POST:
                    current.returnAddress = ReturnAddress.DONE;
                    
                    rt.add(current.param.val);
                    
                default:
                    break;
            }
        }
        
        
        return rt;
    }
}
