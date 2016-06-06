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