# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        deep = 0
        queue = [root]
        while queue:
            deep += 1
            tmpqueue = []
            while queue:
                tmp = queue.pop()
                if tmp.left:
                    tmpqueue.append(tmp.left)
                if tmp.right:
                    tmpqueue.append(tmp.right)
            queue = tmpqueue
        return deep


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        stack = [root]
        res = 1
        while stack:
            while stack[-1].left:
                tmp = stack[-1].left
                stack[-1].left = None
                stack.append(tmp)
            res = max(res, len(stack))
            if stack[-1].right:
                tmp = stack[-1].right
                stack[-1].right = None
                stack.append(tmp)
            else:
                stack.pop()
            res = max(res, len(stack))
        return res
