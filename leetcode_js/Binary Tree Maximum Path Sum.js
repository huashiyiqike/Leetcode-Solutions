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


var maxPathSum = function(root) {
    return helper(root)[0];
 };
function helper(root) {
    console.log(root.val + '  root')
    if(root.left == null && root.right == null) {
        return [root.val, root.val];
    }
    var maxall3 = - Number.MAX_VALUE;
    var maxsingle = - Number.MAX_VALUE;
    var maxall1, maxall2, maxleft, maxright;
    if(root.left != null) {
        [maxall1, maxleft] = helper(root.left);
        maxsingle = Math.max(maxsingle, root.val + maxleft, root.val);
        maxall3 = Math.max(maxall3, maxall1, maxsingle); 
    }
    if(root.right != null) {
        [maxall2, maxright] = helper(root.right);
        maxsingle = Math.max(maxsingle, root.val + maxright, root.val);
        maxall3 = Math.max(maxall3, maxall2, maxsingle); 
    }
   
    if(root.left != null && root.right != null) {
        maxsingle = Math.max(maxsingle, root.val + Math.max(maxleft, maxright), root.val);
        maxall3 = Math.max(maxall3, root.val + maxleft + maxright, maxsingle);
        
    }
   
    return [maxall3, maxsingle];
 }