# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num)==0:
            return None
        tmp=0
        if len(num)%2==1:
            tmp=1
        node=TreeNode(num[int(len(num)/2)+tmp-1])
        node.left=self.sortedArrayToBST(num[:len(num)/2+tmp-1])
        node.right=self.sortedArrayToBST(num[len(num)/2+tmp:])
        return node
