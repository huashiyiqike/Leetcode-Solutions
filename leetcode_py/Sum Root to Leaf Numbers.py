# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def f(self,sum,root):
        if root is None:
            return 0
        sum=10*sum+root.val
        if root.left is None and root.right is None:
            return sum
        else:
            return self.f(sum,root.left)+self.f(sum,root.right)

    def sumNumbers(self, root):
        return self.f(0,root)

class Solution:
    def f(self,root):
        if root == None:
            return []
        res=[]
        if root.left!=None:
            tmpres=self.f(root.left)
            if len(tmpres)>0:
                for i in tmpres:
                    res.append([root.val]+i)

        if root.right!=None:
            tmpres=self.f(root.right)
            if len(tmpres)>0:
                for i in tmpres:
                    res.append([root.val]+i)

        if root.left ==None and root.right==None:
            res.append([root.val])
        return res

    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        lists=self.f(root)
        sum=0
        for i in lists:
            tmp=0
            for idx,item in enumerate(i):
                tmp+=item
                tmp*=10
            sum+=tmp/10
        return sum
        