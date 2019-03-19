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


function levelTraverse(root) {
  let minimum = root.val;
  let queue = [root];
  let tempMin = Number.MAX_VALUE;
  while (queue.length > 0) {
      const newQueue = [];
      for(let i of queue) {

          if(i.val < tempMin && i.val !== minimum) {
              tempMin = i.val;
          }
          
          if(i.left) newQueue.push(i.left);
          if(i.right) newQueue.push(i.right);
      }
  
      queue = newQueue;
  }
  return (tempMin !== minimum && tempMin !== Number.MAX_VALUE ) ? tempMin : -1;
}

var findSecondMinimumValue = function(root) {
  return levelTraverse(root);
};