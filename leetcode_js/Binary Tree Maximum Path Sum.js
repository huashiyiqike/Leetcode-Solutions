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
// return
var helper = function(root, res){
    if(!root) return 0;
    var left = Math.max(0, helper(root.left, res));
    var right = Math.max(0, helper(root.right, res));
    res[0] = Math.max(res[0], root.val + left + right);
    return root.val + Math.max(left, right);
}
var maxPathSum = function(root) {
    var res = [root.val];
    helper(root, res);
    return res[0];
};


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
// return
var helper = function(root, res){
    if(root.left && root.right){
        var leftmaxs = helper(root.left, res);
        var rightmaxs = helper(root.right, res);
        var maxsons = Math.max(leftmaxs, rightmaxs);
        var tmp = Math.max(root.val + leftmaxs + rightmaxs, root.val + Math.max(0, maxsons));
        res[0] = Math.max(res[0], tmp);
        return root.val + (maxsons>0?maxsons:0);
    }
    if(root.right){
        var rightmaxs = helper(root.right, res);
        var tmp = Math.max(root.val, root.val + rightmaxs);
        res[0] = Math.max(res[0], tmp);
        return root.val + (rightmaxs>0?rightmaxs:0);
    }
    if(root.left){
        var rightmaxs = helper(root.left, res);
        var tmp = Math.max(root.val, root.val + rightmaxs);
        res[0] = Math.max(res[0], tmp);
        return root.val + (rightmaxs>0?rightmaxs:0);
    }
    res[0] = Math.max(res[0], root.val);
    return root.val;
}
var maxPathSum = function(root) {
    if(!root) return 0;
    var res = [root.val];
    helper(root, res);
    return res[0];
};