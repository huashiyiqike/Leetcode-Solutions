# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#BFS queue

class Solution:
# @param p, a tree node
# @param q, a tree node
# @return a boolean
def isSameTree(self, p, q):
    if not p and not q: return True
    elif not p or not q: return False



class Solution:
    def f(self,p,q,stack1,stack2):
        while p:
            stack1.append(p)
            if not q:
                return False
            stack2.append(q)
            if p.val!=q.val:
                return False
            q=q.left
            p=p.left
        if q:
            return False
        return True

# @param p, a tree node
# @param q, a tree node
# @return a boolean
    def isSameTree(self, p, q):
        if not p and not q: return True
        elif not p or not q: return False

        stack1 ,stack2= [],[]

        if not self.f(p,q,stack1,stack2):
            return False

        while stack1 and stack2:
            tmp1=stack1.pop(0)
            tmp2=stack2.pop(0)

            if tmp1.right:
                if tmp2.right:
                   if not self.f(tmp1.right,tmp2.right,stack1,stack2):
                       return False
                else:
                    return False
            elif tmp2.right:
                return False
        return True






class Solution:
# @param p, a tree node
# @param q, a tree node
# @return a boolean
def isSameTree(self, p, q):
    if not p and not q: return True
    elif not p or not q: return False

    stack1 = [p]
    stack2 = [q]

    while stack1:
        node1 = stack1.pop()
        node2 = stack2.pop()

        # Check if values are identical
        if node1.val != node2.val:  return False

        # Check if structures are identical
        if (node1.left and not node2.left) or (node1.right and not node2.right) \
                or (not node1.left and node2.left) or (not node1.right and node2.right):
            return False

        # Two nodes have the same structure, push children into stack
        if node1.left:
            stack1.append(node1.left)
            stack2.append(node2.left)

        if node1.right:
            stack1.append(node1.right)
            stack2.append(node2.right)

    # stacks are empty, the whole tree have been checked
    return True


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p==None:
             return q==None
        elif q==None:
             return False
        elif p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        