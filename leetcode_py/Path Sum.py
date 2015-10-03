# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inSum(self,root,sum):
        if root==None:
            return False
        if sum==root.val and root.left==None and root.right==None:
            return True
        left=self.inSum(root.left,sum-root.val)
        right=self.inSum(root.right,sum-root.val)
        return left|right
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        return self.inSum(root,sum)
