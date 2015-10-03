# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        res = []
        if not root:
            return res
        stack = [root]
        last = TreeNode(0)  # not None, careful, None can exist in tree
        while stack:
            tmp = stack[-1]
            if tmp.left == last:
                if tmp.right:
                    stack.append(tmp.right)
                else:
                    res.append(stack.pop().val)
            elif tmp.right == last or (not tmp.left and not tmp.right):
                res.append(stack.pop().val)
            else:
                if tmp.right:
                    stack.append(tmp.right)
                if tmp.left:   # not elif!
                    stack.append(tmp.left)
            last = tmp
        return res

#Morrios remain to be done

# hard to comprehend
#http://blog.csdn.net/linhuanmars/article/details/22009351
# 上面迭代实现的思路虽然清晰，但是实现起来还是分情况太多，不容易记忆。我后来再看wiki的时候发现有跟Binary Tree Inorder Traversal和Binary Tree Preorder Traversal非常类似的解法，容易统一进行记忆，思路可以参考其他两种，区别是最下面在弹栈的时候需要分情况一下：
# 1）如果当前栈顶元素的右结点存在并且还没访问过（也就是右结点不等于上一个访问结点），那么就把当前结点移到右结点继续循环；
# 2）如果栈顶元素右结点是空或者已经访问过，那么说明栈顶元素的左右子树都访问完毕，应该访问自己继续回溯了。
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        stack,cur,pre,res=[],root,None,[]
        while cur or stack:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                if stack[-1].right in (None,pre):
                    res.append(stack[-1].val)
                    pre=stack.pop()
                else:
                    cur=stack[-1].right
        return res


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if not root:
            return []
        stack=[root]
        pre=root
        res=[]
        while stack:
            cur=stack[-1]
            if pre==cur.left:
                if cur.right:
                    stack.append(cur.right)
                    pre=cur.right
                else:
                    stack.pop()
                    res.append(cur.val)
                    pre=cur

            elif pre==cur.right:
                pre=cur
                stack.pop()
                res.append(cur.val)

            else:
                if cur.left:
                    stack.append(cur.left)
                    pre=cur.left
                elif cur.right:
                    stack.append(cur.right)
                    pre=cur.right
                else:
                    pre=cur
                    res.append(cur.val)
                    stack.pop()
        return res



# tree changed
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root ==None:
            return []
        stack=[]
        res=[]
        stack.append(root)
        while len(stack)>0:
            if stack[-1].left!=None:
                stack.append(stack[-1].left)
                stack[-2].left=None
            elif stack[-1].right!=None:
                stack.append(stack[-1].right)
                stack[-2].right=None
            else:
                res.append(stack[-1].val)
                stack.pop()

        return res
