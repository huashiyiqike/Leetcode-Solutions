# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        dummy= ListNode(0)
        dummy.next=head
        pre=dummy
        p=head
        while p:
            if not p.next:
                break
            if p.next.val==p.val:
                while p.next.val==p.val:
                    p=p.next
                    if not p or not p.next:
                        break
                pre.next=p.next
            else:
                pre=p
            p=p.next
        return dummy.next






