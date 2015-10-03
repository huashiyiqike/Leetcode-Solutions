# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        p1,p2=head,head
        while p2!=None:
            p1=p1.next
            p2=p2.next
            if p2==None:
                return False
            else:
                p2=p2.next
            if p1==p2:
                return True
        return False

            
