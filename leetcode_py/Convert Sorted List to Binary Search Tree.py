
# 对于链表，辅助函数可以只传入一个 int 参数，个人认为这样的话更容易理解：
# 辅助函数的调用结果即是把传入的链表指针向前递进 n 步，并返回经过的链表节点转化成的二分查找树的根节点。
#
# class Solution {
# public:
#     TreeNode *sortedListToBST(ListNode *head) {
#     int count = 0;
# for (auto cur = head; cur;) {
#     cur = cur->next;
# ++count;
# }
# return helper(head, count);
# }
# private:
# TreeNode *helper(ListNode *&p, int n) {
# if (!n) return NULL;
# auto left = helper(p, n / 2);
# auto res = new TreeNode(p->val);
# p = p->next;
# res->left = left;
# res->right = helper(p, n - n / 2 - 1);
# return res;
# }
# };

# not right, p changed in c++ while head not changed in python
# class Solution:
#     def f(self,head,num):
#         if num<=0:
#             return None
#         left=self.f(head,num/2)
#         res=TreeNode(head.val)
#         head=head.next
#         res.left,res.right=left,self.f(head,num-num/2-1)
#         return res
#
#     # @param {ListNode} head
#     # @return {TreeNode}
#     def sortedListToBST(self, head):
#         tmp,num=head,0
#         while tmp:
#             tmp=tmp.next
#             num+=1
#
#         return self.f(head,num)

#bottom up
class Solution:
    def f(self,l,r):
        if l>r:
            return None
        m=(l+r)/2

        left=self.f(l,m-1)
        a=TreeNode(self.start.val)
        self.start=self.start.next
        right=self.f(m+1,r)

        a.left,a.right=left,right
        return a

    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if head is None:
            return None
        self.start=head

        tmp,count=head,0
        while tmp:
            count+=1
            tmp=tmp.next
        return self.f(0,count-1)


class Solution:
    def create(self,head,lens):
        if lens==0 or head is None:
            return None
        if lens==1:
            return TreeNode(head.val)

        tmp=head
        for i in range((lens-1)/2):
            tmp=tmp.next

        res=TreeNode(tmp.val)
        res.left=self.create(head,(lens-1)/2)
        res.right=self.create(tmp.next,lens/2)
        return res
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head is None:
            return None

        tmp=head
        lens=0
        while tmp:
            lens+=1
            tmp=tmp.next

        return self.create(head,lens)
