# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTravel(self,root,last):
        if root is None:
            return None,None
        if root.left:
            last=self.inorderTravel(root.left,  last)
        if last.val>root.val:
            if self.first is None:
                self.first=last
                self.second=root
            else:
                self.second=root
        last=root
        if root.right:
            last=self.inorderTravel(root.right, last)
        return last

    def recoverTree(self,root):
        self.first,self.second=None,None
        dummy=TreeNode(-1<<64) # or set as None
        self.inorderTravel(root,dummy)
        self.first.val,self.second.val=self.second.val,self.first.val


if __name__=="__main__":
    a=Solution()
    m=TreeNode(0)
    n=TreeNode(1)
    m.left=n
    a.recoverTree(m)
    print m.val
    print n.val
