/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
  var res = [], stack = [], cur = root;
  while(stack.length > 0 || cur !== null ){
      if(cur !== null){
          stack.push(cur);
          cur = cur.left;
      }else{
          cur = stack.pop();
          res.push(cur.val);
           k -= 1;
          if(k===0) {
              return cur.val;
          }
          cur = cur.right;
      }
  }
  return res;
};
