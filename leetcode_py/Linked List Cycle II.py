# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        if head.next==head:
            return head
        if head.next.next==head:
            return head
        if head.next.next==None:
            return None
            
        pre=head.next.next
        last=head
        First=True
        count=0
        while pre.next is not None and pre.next.next is not None:
            pre=pre.next.next
            last=last.next
            if First ==False:
                count+=1
            if pre==last:
                if First==True:
                    First=False
                else:
                    break
        if count!=0:
            pre=head
            last=head
            for i in range(count):
                pre=pre.next
            while pre!=last:
                pre=pre.next
                last=last.next
            return last
        else:
            return None


#    https://leetcode.com/discuss/18393/share-complexity-constant-space-code-original-list-comments
class Solution:
    def detectCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None