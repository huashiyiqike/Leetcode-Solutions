public class Solution {
    public List<Integer> rightSideView(TreeNode root) {
         List<Integer> result = new ArrayList<Integer>();
        if(root == null){
            return result;
        }
        dfs(result,root,0);
        return result;
    }
    public void dfs( List<Integer> result,TreeNode node,int level){
        if(node == null){
            return ;
        }
        if(result.size() == level){
            result.add(node.val);
        }
      
        dfs(result,node.right,level+1);
        dfs(result,node.left,level+1);
        
    }
}