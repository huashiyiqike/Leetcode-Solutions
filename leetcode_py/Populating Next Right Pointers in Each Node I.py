# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# only preorder or level order can make it
# preorder
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root or not root.left:
            return
        root.left.next = root.right
        root.right.next = root.next.left if root.next else None
        self.connect(root.left)
        self.connect(root.right)

# level order
class Solution:
    def helper(self, root):
        if not root:
            return
        while root:
            if not root.left:
                return
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
            root = root.next
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        while root:
            self.helper(root)
            root = root.left