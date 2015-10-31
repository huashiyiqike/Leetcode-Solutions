# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTravel(self, root, last):
        if root.left:
            last = self.inorderTravel(root.left, last)
        if last and last.val > root.val:
            if self.first is None:
                self.first = last
            self.second = root
        last = root
        if root.right:
            last = self.inorderTravel(root.right, last)
        return last

    def recoverTree(self, root):
        if root is None:
            return
        self.first, self.second = None, None
        self.inorderTravel(root, None)
        self.first.val, self.second.val = self.second.val, self.first.val


if __name__ == "__main__":
    a = Solution()
    m = TreeNode(0)
    n = TreeNode(1)
    m.left = n
    a.recoverTree(m)
    print m.val
    print n.val
