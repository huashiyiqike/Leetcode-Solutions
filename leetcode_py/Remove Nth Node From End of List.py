# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if n == 0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        nextn = dummy
        for i in range(n):
            nextn = nextn.next
        while nextn.next:
            pre = pre.next
            nextn = nextn.next
        pre.next = pre.next.next
        return dummy.next
