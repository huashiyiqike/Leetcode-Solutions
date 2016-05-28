# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, root, left, right):
        if not root:
            return True
        if root.val <= left or root.val >= right:
            return False
        return self.helper(root.left, left, root.val) and self.helper(root.right, root.val, right)

    def isValidBST(self, root):
        return self.helper(root, float("-inf"), float("inf"))
