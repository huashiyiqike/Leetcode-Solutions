# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#iterative
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        q1,q2=[root],[root]
        while q1 or q2:
            if q1[0] is None and q2[0] is None:
                q1.pop(0)
                q2.pop(0)
            elif q1[0] is None or q2[0] is None or q1[0].val !=q2[0].val:
                return False
            else:
                q1+=[q1[0].left,q1[0].right]
                q2+=[q2[0].right,q2[0].left]
                q1.pop(0)
                q2.pop(0)
        return True


if __name__=="__main__":
    a=Solution()
    m=TreeNode(1)
    print a.isSymmetric(m)

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricRecur(root.left, root.right)

    def isSymmetricRecur(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRecur(left.left, right.right) and self.isSymmetricRecur(left.right, right.left)


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root:
            return True
        q = [root.left, root.right]
        while q:
            left = q.pop()
            right = q.pop()
            if not left and not right:
                continue
            elif not left or not right or left.val != right.val:
                return False
            else:
                q += [left.left, right.right, left.right, right.left]
        return True

