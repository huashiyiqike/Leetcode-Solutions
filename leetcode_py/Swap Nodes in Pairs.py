# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        p = head
        while head:
            if head.next:
                tmp = head.next.val
                head.next.val = head.val
                head.val = tmp
                head = head.next.next
            else:
                return p
        return p


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return None
        if not head.next:
            return head

        newhead = head.next
        tmp = head.next.next
        newhead.next = head
        head.next = self.swapPairs(tmp)

        return newhead


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        p = head
        while p and p.next:
            pre.next = p.next
            p.next = p.next.next
            pre.next.next = p

            pre = p
            p = p.next
        return dummy.next


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if not cur.next.next:
                return dummy.next
            tmp = cur.next.next.next
            cur.next.next.next = cur.next
            cur.next = cur.next.next
            cur.next.next.next = tmp
            cur = cur.next.next
        return dummy.next


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        pre = head
        p = head.next
        head = p
        while p:
            tmp = p.next
            p.next = pre
            if tmp:
                if tmp.next:
                    pre.next = tmp.next
                else:
                    pre.next = tmp
                    return head
                pre = tmp
                p = tmp.next
            else:
                pre.next = None
                return head

        return head
