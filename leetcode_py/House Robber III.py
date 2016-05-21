# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def depthFirst(root):
    if root == None:
        return 0

    root.val += depthFirst(root.left)
    root.val += depthFirst(root.right)
     
    next = (root.left.val if root.left!=None else 0) +  (root.right.val if root.right else 0)
    root.val = max(next, root.val);
    return next;


class Solution(object):
    def rob(self, root):
        if not root:
            return 0
        """
        :type root: TreeNode
        :rtype: int
        """
        depthFirst(root)
        return root.val

if __name__=="__main__":
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    a = Solution()
    print a.rob(root)