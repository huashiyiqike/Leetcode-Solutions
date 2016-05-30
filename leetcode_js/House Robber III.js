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


function depthFirst(root){
    if(root == undefined) return 0;

    root.val += depthFirst(root.left);
    root.val += depthFirst(root.right);
     
    next = (root.left!=undefined?root.left.val:0)+(root.right!=undefined?root.right.val:0)
    root.val = Math.max(next, root.val);
    return next;
}
var rob = function(root) { 
    if(root == undefined) return 0;
    depthFirst(root);
    return root.val;
};


 // this will TLE
 
function depthFirst(root){
    if(root == undefined) return 0;
    var res_y = root.val;
    if(root.left != undefined) {
        res_y += depthFirst(root.left.left);
        res_y += depthFirst(root.left.right);
    }
    if(root.right != undefined){
       res_y += depthFirst(root.right.left);
       res_y += depthFirst(root.right.right);
    }
   
    var res_n = 0;
    res_n += depthFirst(root.left);
    res_n += depthFirst(root.right);
    return Math.max(res_y, res_n);
}
  

 
