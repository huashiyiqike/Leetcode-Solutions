# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        res = []
        reverse = False
        while queue:
            count = len(queue)
            tmp = []
            next = []
            for i in range(count):
                if queue[i].left:
                    next.append(queue[i].left)
                if queue[i].right:
                    next.append(queue[i].right)
                tmp.append(queue[i].val)

            if not reverse:
                res.append(tmp)
                reverse = True
            else:
                res.append(tmp[::-1])
                reverse = False
            queue = next

        return res
