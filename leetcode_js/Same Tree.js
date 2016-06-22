/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    if(p != undefined && q != undefined && p.val == q.val){
    	return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }else if(p == undefined && q == undefined){
    	return true;
    }
    return false;
};