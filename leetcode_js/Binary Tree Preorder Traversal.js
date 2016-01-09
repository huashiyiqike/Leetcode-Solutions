/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {
    var res = [], stack = [];
    while(root !== null || stack.length > 0){
        if(root !== null){
            res.push(root.val);
            if(root.right !== null) stack.push(root.right);
            root = root.left;
        }else{
            root = stack.pop();
        }
    }
    return res;
};