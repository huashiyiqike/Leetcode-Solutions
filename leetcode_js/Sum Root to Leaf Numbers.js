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
var helper = function(root, res, path){
    path = path * 10 + root.val;
    if(!root.left && !root.right){
        res[0] += path;
        return;
    }
    if(root.left){
        helper(root.left, res, path);
    }
    if(root.right){
        helper(root.right, res, path);
    }
}
var sumNumbers = function(root) {
    if(!root) return 0;
    var res = [0];
    helper(root, res, 0);
    return res[0];
};