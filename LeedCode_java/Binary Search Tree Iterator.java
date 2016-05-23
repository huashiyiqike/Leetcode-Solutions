/*
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
*/

public class BSTIterator {
private Stack<TreeNode> stack;
    public BSTIterator(TreeNode root) {
        stack=new Stack<TreeNode>();
        smallStack(root);
    }
  public void smallStack(TreeNode root){
      if(root!=null){
          stack.push(root);
          root=root.left;
          smallStack(root);
      }
  }
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        if(!stack.isEmpty()){
            return true;
        }
        return false;
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode node=stack.pop();
        smallStack(node.right);
        return node.val;
    }
}