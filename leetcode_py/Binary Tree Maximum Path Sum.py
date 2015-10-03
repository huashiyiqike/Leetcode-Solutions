# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def __init__(self):
        self.max = -1<<64

    def helper(self, root):
        if not root:
            return 0
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)
        self.max = max(self.max, left + right + root.val)
        return max(left, right) + root.val

    def maxPathSum(self,root):
        self.helper(root)
        return self.max


class Solution:
    def __init__(self):
        self.max = -1<<64

    def helper(self, root):
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)
        self.max = max(self.max, left + right + root.val)
        return max(left, right) + root.val

    def maxsum(self,root):
        self.helper(root)
        return self.max


class Solution:
    def f(self,root):
        if not root:
            return -1<<64,0
        lmax,l=self.f(root.left)
        rmax,r=self.f(root.right)
        tmp=max(l+root.val,r+root.val,root.val)
        return max(lmax,rmax,tmp,l+r+root.val),tmp

    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        return self.f(root)[0]


class Solution:
    def maxsum(self,root):
        if root is None:
            return -2<<64
        left=self.maxsum(root.left)
        right=self.maxsum(root.right)
        self.maxs=max(self.maxs,left,right,root.val+left+right)
        return max(root.val,root.val+left,root.val+right)
  
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root is None:
            return 0
        self.maxs=-2<<64
        return max(self.maxsum(root),self.maxs)

if __name__=="__main__":
    a=Solution()
    tree=TreeNode(-2)
    tree.left=TreeNode(1)
    print a.maxPathSum(tree)
    print a.maxPathSum(tree.left)
