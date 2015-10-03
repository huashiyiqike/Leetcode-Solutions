# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def f(self,root):
        if root==None:
            return 0
        left=self.f(root.left)
        right=self.f(root.right)
        if abs(left-right)>=2 or left==-1 or right==-1:
            return -1
        else:
            return max(left,right)+1
    def isBalanced(self, root):
        return self.f(root)>=0

class Solution:
    def in_isBalanced(self,root):
        if root.left!=None and root.right!=None:
            left=self.in_isBalanced(root.left)
            right=self.in_isBalanced(root.right)
            if abs(left-right)<=1 and left!=2<<64:
                return 1+max(left,right)
            else:
                return 2<<64
        elif root.right!=None:
            tmp=self.in_isBalanced(root.right)
            if tmp<=1:
                return 1+tmp
            else:
                return 2<<64
        elif root.left!=None:
            tmp=self.in_isBalanced(root.left)
            if tmp<=1:
                return 1+tmp
            else:
                return 2<<64
        else:
            return 1



    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root==None:
            return True
        if root.left!=None and root.right!=None:
            return abs(self.in_isBalanced(root.left)-self.in_isBalanced(root.right))<=1 and self.in_isBalanced(root.left)!=2<<64
        elif root.left!=None:
            return self.in_isBalanced(root.left)<=1
        elif root.right!=None:
            return self.in_isBalanced(root.right)<=1
        else:
            return True
        
            
