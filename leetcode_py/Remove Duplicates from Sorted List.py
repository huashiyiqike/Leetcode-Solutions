
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        dummy=ListNode(0)
        dummy.next=head
        p=dummy.next
        while p.next:
            if p.next.val==p.val:
                p.next=p.next.next
            else:
                p=p.next
        return dummy.next