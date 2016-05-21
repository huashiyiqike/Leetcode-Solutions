/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

 // TLE
var rob = function(root) {
    return depthFirst(root);
};

function depthFirst(root){
    if(root == undefined) return 0;
    var res_y = root.val;
    if(root.left != undefined) {
        res_y += depthFirst(root.left.left);
        res_y += depthFirst(root.left.right);
    }
    if(root.right != undefined){
       res_y += depthFirst(root.right.left);
       res_y += depthFirst(root.right.right);
    }
   
    var res_n = 0;
    res_n += depthFirst(root.left);
    res_n += depthFirst(root.right);
    return Math.max(res_y, res_n);
}
 
function depthFirst(root):
    if(root == None) return 0;

    root.val += depthFirst(root.left)
    root.val += depthFirst(root.right)
     
    next = (root.left!=None?root.left.val:0)+(root.right!=None?root.right.val:0)
    root.val = max(next, root.val);
    return next;


class Solution(object):
    def rob(self, root):
        if not root:
            return 0
        """
        :type root: TreeNode
        :rtype: int
        """
        depthFirst(root)
        return root.val
