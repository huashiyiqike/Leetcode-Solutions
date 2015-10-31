# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        dummychild = TreeLinkNode(0)
        while root:
            cur = dummychild
            dummychild.next = None
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            root = dummychild.next


class Solution:
    def first(self, root):
        while root:
            if root.left:
                return root.left
            elif root.right:
                return root.right
            root = root.next
        return None

    def helper(self, root):
        if not root:
            return
        while root:
            if root.left:
                root.left.next = root.right if root.right else self.first(root.next)
            if root.right:
                root.right.next = self.first(root.next)
            root = root.next

    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        while root:
            self.helper(root)
            root = self.first(root)


# not O(1)
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        lists = []
        lists.append(root)
        while lists:
            next = []
            for i, item in enumerate(lists):
                if i != 0:
                    lists[i - 1].next = lists[i]
                if i == len(lists) - 1:
                    lists[i].next = None
                if item.left:
                    next.append(item.left)
                if item.right:
                    next.append(item.right)
            lists = next
