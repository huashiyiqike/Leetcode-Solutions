# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q or not root:
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if left and right:
                return root
            elif left:
                return left
            else:
                return right

# too much redundant traversal
# class Solution:
#     def helper(self, root, x):
#         if root == x:
#             return True
#         elif not root:
#             return False
#         return self.helper(root.left, x) or self.helper(root.right, x)
#
#     # @param {TreeNode} root
#     # @param {TreeNode} p
#     # @param {TreeNode} q
#     # @return {TreeNode}
#     def lowestCommonAncestor(self, root, p, q):
#         if self.helper(root.left, p) and self.helper(root.left, q):
#             return self.lowestCommonAncestor(root.left, p, q)
#         if self.helper(root.right, p) and self.helper(root.right, q):
#             return self.lowestCommonAncestor(root.right, p, q)
#
#         return root
#
