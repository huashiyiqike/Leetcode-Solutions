# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        left_p, right_p = root, root
        left_count,right_count = 0, 0
        while left_p:
            left_p=left_p.left
            left_count+=1
        while right_p:
            right_p=right_p.right
            right_count+=1
        if left_count==right_count:
            return 2**left_count - 1
        else:
            return 1 + self.countNodes(root.left)+self.countNodes(root.right)

class Solution:
    def getheight(self, root):
        count = 0
        while root:
            root = root.left
            count += 1
        return count

    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        res=0
        while root:
            h = self.getheight(root.left)
            h_subright = self.getheight(root.right)
            if h == h_subright:
                res += 2 ** h
                root = root.right
            else:
                res += 2 ** (h - 1)
                root = root.left
        return res

# binary search
class Solution:
    def getheight(self, root):
        count = 0
        while root:
            root = root.left
            count += 1
        return count

    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        h = self.getheight(root.left)
        h_subright = self.getheight(root.right)
        if h == h_subright:
            return 2 ** h + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + 2 ** (h - 1)

#TLE
class Solution:
    def f(self, root, left_count, right_count):
        if not root:
            return 0

        left_p, right_p = root, root
        if left_count == -1:
            left_count = 0
            while left_p:
                left_p = left_p.left
                left_count += 1

        if right_count == -1:
            right_count = 0
            while right_p:
                right_p=right_p.right
                right_count += 1

        if left_count == right_count:
            return 2**left_count
        else:
            return self.f(root.left, left_count-1, -1)+self.f(root.right, -1, right_count-1)

    def countNodes(self, root):
        return self.f(root, -1, -1)