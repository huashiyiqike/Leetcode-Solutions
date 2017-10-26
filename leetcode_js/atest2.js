
 function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

/**
* @param {TreeNode} root
* @return {number}
*/
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
       console.log('root ' + root.val +  ' left' + maxall1)
   }
   if(root.right != null) {
       [maxall2, maxright] = helper(root.right);
       maxsingle = Math.max(maxsingle, root.val + maxright, root.val);
       maxall3 = Math.max(maxall3, maxall2, maxsingle);
       console.log('root ' + root.val +  ' right' + maxall2)
   }
  
   if(root.left != null && root.right != null) {
       maxsingle = Math.max(maxsingle, root.val + Math.max(maxleft, maxright), root.val);
       maxall3 = Math.max(maxall3, root.val + maxleft + maxright, maxsingle);
       console.log(root.val + '  root')
       console.log('max ' +maxall3 + ' maxleft ' + maxall1 + ' maxright ' + maxall2);
   }
  
   return [maxall3, maxsingle];
}


root = new  TreeNode(1);
root.left = new TreeNode(-2)
root.left.left = new TreeNode(1)
root.left.left.left = new TreeNode(-1)
root.left.right = new TreeNode(3)
root.right = new TreeNode(-3)
root.right.left = new TreeNode(-2)
console.log(maxPathSum(root))