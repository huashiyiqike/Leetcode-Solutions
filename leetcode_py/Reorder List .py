# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if not head or not head.next:
            return
        fast = head
        slow = head
        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
                slow = slow.next

        dummy = ListNode(0)
        dummy.next = slow.next
        slow.next = None

        cur = dummy.next
        while cur.next:
            tmp = cur.next.next
            cur.next.next = dummy.next
            dummy.next = cur.next
            cur.next = tmp

        cur = dummy
        while cur.next:
            tmp = cur.next.next
            cur.next.next = head.next
            head.next = cur.next
            head = head.next.next
            cur.next = tmp

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if not head or not head.next:
            return
        dummy=ListNode(0)
        dummy.next=head
        p1,p2=dummy,dummy
        while p2 and p2.next:
            p1=p1.next
            p2=p2.next
            p2=p2.next

        p2=p1.next
        while p2.next:
            tmp=p2.next
            p2.next=p2.next.next
            tmp.next=p1.next
            p1.next=tmp

        p2=p1.next


        p1.next=None
        pre=ListNode(0)
        while head :
            pre.next=head
            head=head.next
            if p2:
                pre.next.next=p2
                pre=p2
                p2=p2.next
            else:
                break
