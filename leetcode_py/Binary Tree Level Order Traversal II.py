# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None:
            return []
        res = []
        queue = [root]
        while queue:
            current = []
            tmpres = []
            for i in queue:
                if i.left:
                    current.append(i.left)
                if i.right:
                    current.append(i.right)
                tmpres.append(i.val)
            queue = current
            res = [tmpres] + res
        return res


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None:
            return []
        res = []
        queue = [root]
        while queue:
            count = len(queue)
            tmp = []
            for i in range(count):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                tmp.append(queue.pop(0).val)
            res.insert(0, tmp)
        return res
