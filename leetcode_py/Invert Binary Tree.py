# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        stack=[root]
        while stack:
            tmp=stack.pop()
            if not tmp:
                continue
            tmp.left,tmp.right=tmp.right,tmp.left
            stack.append(tmp.left)
            stack.append(tmp.right)
        return root


class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return root
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root