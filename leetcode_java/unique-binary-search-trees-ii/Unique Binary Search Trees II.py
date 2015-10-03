# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# recursive
class Solution:
    def f(self,start,end):
        if start>end:
            return [None]
        res=[]
        for i in range(start,end+1):
            left=self.f(start,i-1)
            right=self.f(i+1,end)

            for m in left:
                for j in right:
                    a=TreeNode(i)
                    a.left=m
                    a.right=j
                    res.append(a)
        return res

    def generateTrees(self, n):
        return self.f(1,n)

