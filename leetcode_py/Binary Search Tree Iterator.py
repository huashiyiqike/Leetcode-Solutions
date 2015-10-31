# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.stack) > 0:
            return True

    # @return an integer, the next smallest number
    def next(self):
        res = self.stack[-1]
        tmp = self.stack.pop()
        tmp = tmp.right
        if tmp:
            self.stack.append(tmp)
            while tmp.left:
                self.stack.append(tmp.left)
                tmp = tmp.left
        return res.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
# 
# class BSTIterator:
#     def travel(self,root):
#         if root==None:
#             return
#         if root.left:  self.parent[root.left]=root;self.travel(root.left)
#         if root.right:  self.parent[root.right]=root;self.travel(root.right)
#     # @param root, a binary search tree's root node
#     def __init__(self, root):
#         self.parent={}
#         self.travel(root)
#         self.pointer=root
#         #self.parent[root]=root
#         self.root=root
#         self.first=True
#         
# 
#     # @return a boolean, whether we have a next smallest number
#     def hasNext(self):
#         if self.pointer==None:
#             return None
#         if self.first:
#             self.first=False
#             while self.pointer.left:
#                 self.pointer=self.pointer.left
#             return True
#         if self.pointer.right: 
#             tmp=self.pointer.right;
#             while tmp.left:
#                 tmp=tmp.left
#             self.pointer=tmp
#             return True
#         else:
#             #print self.pointer.val
#             if self.pointer ==self.root:#not in  self.parent.keys():
#                 return False
#             elif self.parent[self.pointer].left==self.pointer:
#                 self.pointer=self.parent[self.pointer]
#                 return True
#             else:
#                 while  self.pointer==self.parent[self.pointer].right:
#                     self.pointer=self.parent[self.pointer]
#                     if self.pointer==self.root:# not in self.parent.keys()  :
#                         return False
#                 if self.pointer !=self.root:#in self.parent.keys():
#                     self.pointer=self.parent[self.pointer]
#                     return True
#                 return False
# #                     
# 
#     # @return an integer, the next smallest number
#     def next(self):
#         return self.pointer.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
if __name__ == "__main__":

    m = TreeNode(3)
    p = TreeNode(1)
    n = TreeNode(4)
    k = TreeNode(2)
    m.right = n
    m.left = p
    p.right = k
    a = BSTIterator(m)
    while a.hasNext():
        print a.next()
