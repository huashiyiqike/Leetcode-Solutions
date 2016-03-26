/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[]}
 */

var helper = function(root, path, res){
    if(!root) return;
    var tmppath = path+root.val+'->';
    if(!root.left && !root.right){
        res.push(tmppath.length>0?tmppath.substr(0, tmppath.length-2):'');
        return;
    }
    if(root.left){
        helper(root.left, tmppath, res);
    }
    if(root.right){
        helper(root.right, tmppath, res);
    }
}
var binaryTreePaths = function(root) {
    var res = [];
    helper(root, '', res);
    return res;
};
root = new TreeNode(1)
root.left = new TreeNode(2);
console.log(binaryTreePaths(root))