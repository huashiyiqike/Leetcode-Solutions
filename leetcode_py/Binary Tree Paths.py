# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# note that if judged too late, i.e. at the leaf, the answer will be doubled.

class Solution(object):
    def helper(self, cur, path, res):
        newpath = path + str(cur.val) + '->'
        if not cur.left and not cur.right:
            if len(newpath) > 2:
                res.append(newpath[:-2])
        else:
            if cur.left:
                self.helper(cur.left, newpath, res)
            if cur.right:
                self.helper(cur.right, newpath, res)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.helper(root, '', res)
        return res
