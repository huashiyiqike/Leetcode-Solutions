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
var helper = function(root, res){
    if(!root) return;
    helper(root.left, res);
    res.push(root.val);
    helper(root.right, res);
}
var inorderTraversal = function(root) {
    var res = [];
    helper(root, res);
    return res;
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
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    var res = [], stack = [], cur = root;
    while(stack.length > 0 || cur !== null ){
        if(cur !== null){
            stack.push(cur);
            cur = cur.left;
        }else{
            cur = stack.pop();
            res.push(cur.val);
            cur = cur.right;
        }
    }
    return res;
};