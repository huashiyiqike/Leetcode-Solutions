# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# inplace
class Solution:
    def helper(self, root, pre):
        pre.right = root
        tmp = root.right
        if root.left:
            pre = self.helper(root.left, root)
        else:
            pre = root
        if tmp:
            pre = self.helper(tmp, pre)
        root.left = None  # do not forget this
        return pre

    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return
        pre = TreeNode(0)
        self.helper(root, pre)


# inplace
class Solution:
    def f(self, root):
        if not root.left and not root.right:
            return root
        tmp = root.right
        last = None
        if root.left:
            last = self.f(root.left)
            last.right = root.right
            root.right = root.left
            root.left = None
        if tmp:
            last2 = self.f(tmp)
        else:
            if last:
                last2 = last
            else:
                last2 = root

        return last2

    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root or (not root.left and not root.right):
            return
        self.f(root)


class Solution:
    last = None

    def flatten(self, root):
        if root != None:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.last
            root.left = None
            self.last = root


class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return
        stacks = [root]
        while len(stacks) > 0:
            p = stacks.pop()
            if p.right:
                stacks.append(p.right)
            while p.left:
                p.right = p.left
                p.left = None
                p = p.right
                if p.right:
                    stacks.append(p.right)
            if stacks:
                p.right = stacks[-1]


class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        stack = []
        if root is None:
            return
        stack.append(root)
        while len(stack) > 0:
            tmp = stack.pop()

            if tmp.left:
                while tmp.left:
                    if tmp.right:
                        stack.append(tmp.right)
                    tmp.right = tmp.left
                    tmp.left = None
                    tmp = tmp.right

                stack.append(tmp)

            elif tmp.right:
                stack.append(tmp.right)

            else:
                if len(stack) > 0:
                    tmp.right = stack[-1]
                else:
                    tmp.right = None

                tmp.left = None
