# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def f(self, inorder, postorder, i, j, k, l):
        if i > j:
            return None
        root = TreeNode(postorder[l])
        m = inorder.index(postorder[l])
        root.left = self.f(inorder, postorder, i, m - 1, k, k + m - 1 - i)
        root.right = self.f(inorder, postorder, m + 1, j, l - j + m, l - 1)
        return root

    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        return self.f(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)
