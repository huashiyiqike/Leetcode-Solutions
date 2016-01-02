# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def ins(self, root, target, path, res):
        if root is None:
            return res
        if root.val == target and root.left is None and root.right is None:
            return res + [path + [root.val]]
        else:
            return self.ins(root.left, target - root.val, path + [root.val], res) + \
                   self.ins(root.right, target - root.val, path + [root.val], res)

    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        return self.ins(root, sum, [], [])
        # return res


if __name__ == "__main__":
    a = Solution()
    a.ins()


class Solution:
    def ins(self, root, target, lists):
        if root is None:
            return
        if root.val == target and root.left is None and root.right is None:
            self.res.append(lists + [root.val])
        else:
            if root.left is not None:
                tmp = [i for i in lists]
                self.ins(root.left, target - root.val, tmp + [root.val])
            if root.right is not None:
                tmp = [i for i in lists]
                self.ins(root.right, target - root.val, tmp + [root.val])

    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        self.res = []
        if root is None:
            return []
        self.ins(root, sum, [])
        return self.res
