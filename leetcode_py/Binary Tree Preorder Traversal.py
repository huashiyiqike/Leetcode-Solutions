# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        stack=[]
        cur=root
        res=[]
        while cur or stack:
            while cur:
                res.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                cur=cur.left
            if stack:
                cur=stack.pop()
        return res

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        stack,res,current=[],[],root
        while stack or current:
            if current:
                res.append(current.val)
                if current.right:
                    stack.append(current.right)
                current = current.left
            else:
                current=stack.pop()
        return res

#first in, last out, the direct way
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        stack=[root]
        res=[]
        while stack:
            cur=stack.pop()
            if not cur:
                continue
            res.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
        return res


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        current =root 
        res=[]
        while current:
            if current.left==None:
                res.append(current.val)
                current=current.right
            else:
                pre=current.left 
                
                while pre.right and pre.right!=current:
                    pre=pre.right
                if pre.right is None:
                    pre.right=current 
                    res.append(current.val)
                    current=current.left
                else:
                    pre.right=None
                    current=current.right 
        return res

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        tmplist=[]
        if root==None:
            return tmplist
        tmplist.append(root.val)
        if root.left!=None:
            tmplist+=self.preorderTraversal(root.left)
        if root.right!=None:
            tmplist+=self.preorderTraversal(root.right)
        return tmplist

if __name__=='__main__':
    a=Solution()
    tree=TreeNode(1)
    tree2=TreeNode(2)
    tree.right=tree2
    print a.preorderTraversal(tree)
           
