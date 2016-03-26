/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {boolean}
 */
var helper = function(root, sum){
    if(!root.left && !root.right){
        return root.val === sum;
    }else return (!!root.left && helper(root.left, sum - root.val)) ||
     (!!root.right && helper(root.right, sum - root.val));
}
var hasPathSum = function(root, sum) {
    if(!root) return false;
    return helper(root, sum);
};