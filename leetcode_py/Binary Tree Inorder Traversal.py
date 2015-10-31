# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        lists = []
        res = []
        while root:
            lists.append(root)
            root = root.left

        while lists:
            tmp = lists[-1]
            lists.pop()
            res.append(tmp.val)
            if tmp.right:
                tmp = tmp.right
                while tmp:
                    lists.append(tmp)
                    tmp = tmp.left

        return res

        # DFS


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack, res, current = [], [], root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                res.append(current.val)
                current = current.right

        return res


# Morris Travel # changed tree structure
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        current = root
        res = []
        while current:
            if current.left == None:
                res.append(current.val)
                current = current.right
            else:
                pre = current.left

                while pre.right and pre.right != current:
                    pre = pre.right
                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    res.append(current.val)
                    current = current.right
        return res


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):

        tmplist = []

        if root == None:
            return tmplist

        if root.left != None:
            tmplist += self.inorderTraversal(root.left)

        tmplist.append(root.val)

        if root.right != None:
            tmplist += self.inorderTraversal(root.right)
        return tmplist
