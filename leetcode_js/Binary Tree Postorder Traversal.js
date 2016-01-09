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
var postorderTraversal = function(root) {
    var res = [], stack = [], cur = root, pre = null;
    while(stack.length > 0 || cur !== null){
        if(cur){ 
            stack.push(cur);
            cur = cur.left;
        }else{
            if(pre === stack[stack.length-1].right || stack[stack.length-1].right === null){  
                pre = stack.pop();
                res.push(pre.val);
            }else{
                cur = stack[stack.length-1].right;
            }
        }
    }
    return res;
};