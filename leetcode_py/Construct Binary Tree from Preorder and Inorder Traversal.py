# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder)==0:
            return None
        return self.buildTree_help(preorder, inorder, 0,len(inorder)-1, 0,len(inorder)-1)

    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree_help(self, preorder, inorder,i,j,k,l):
        if i>j:
            return None
        # for idx in range(k,l+1):
        #     if inorder[idx]==preorder[i]:
        #         root_idx=idx
        root_idx=inorder.index(preorder[i])

        root=TreeNode(inorder[root_idx])
        root.left=self.buildTree_help(preorder, inorder,   i+1,         i+root_idx-k,      k,    root_idx-1)
        root.right=self.buildTree_help(preorder,inorder,  j-l+root_idx+1,    j,      root_idx+1,         l)
        return root

if __name__=="__main__":
    a=Solution()
    print a.buildTree([2,3], [2,3])

#  MLE
class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder)==0:
            return None

        for idx,item in enumerate(inorder):
            if item==preorder[0]:
                root_idx=idx
                break
        root=TreeNode(inorder[root_idx])
        root.left=self.buildTree(preorder[1:root_idx+1],inorder[:root_idx])
        root.right=self.buildTree(preorder[root_idx+1:],inorder[root_idx+1:])
        return root

# https://leetcode.com/discuss/28271/my-o-n-19ms-solution-without-recusion-hope-help-you
# class Solution:
#     # @param preorder, a list of integers
#     # @param inorder, a list of integers
#     # @return a tree node
#     def buildTree(self, preorder, inorder):
#         stack=[]
#         root=TreeNode(0)
#         if len(preorder)==0:
#             return None
#         root=TreeNode(preorder[0])
#         stack.append(root)
#         index=0
#         for i in range(1,len(preorder)+1):
#             cur=stack[-1]
#             if(stack[-1].val!=inorder[index]):
#                 cur.left=TreeNode(preorder[i])
#                 stack.append(cur.left)
#             else:
#                 while(len(stack)!=0 and stack[-1].val==inorder[index]):
#                     cur=stack[-1]
#                     stack.pop()
#                     index+=1
#                 if(index<len(inorder)):
#                     cur.right=TreeNode(preorder[i])
#                     stack.append(cur.right)
#
#         return root
