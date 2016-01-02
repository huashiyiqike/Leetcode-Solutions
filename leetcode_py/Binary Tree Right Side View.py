# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if root == None:
            return []
        now = [root]
        res = []
        while len(now) > 0:
            next = []
            for i in now:
                if i.left:
                    next.append(i.left)
                if i.right:
                    next.append(i.right)
            res.append(now[-1].val)
            now = next
        return res


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if root == None:
            return []
        now = [root]
        next = []
        res = []
        while len(now) > 0:
            if now[0].left != None:
                next.append(now[0].left)
            if now[0].right != None:
                next.append(now[0].right)

            tmp = now[0].val
            now.pop(0)
            if len(now) == 0:
                res.append(tmp)
                now = next
                next = []
        return res
