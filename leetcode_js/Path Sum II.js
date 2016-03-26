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
 * @return {number[][]}
 */
function helper(root, sum, path, res){
    path = path.concat(root.val);
    if(!root.left && !root.right){
        if(root.val === sum){
            res.push(path);
        }
        return;
    }
    if(root.left){
        helper(root.left, sum - root.val, path, res);
    }
     if(root.right){
        helper(root.right, sum - root.val, path, res);
    }
}
var pathSum = function(root, sum) {
    if(!root) return [];
    var res = [];
    helper(root, sum, [], res);
    return res;
};