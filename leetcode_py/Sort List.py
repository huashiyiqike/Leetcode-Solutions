# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self, p, q):
        head = ListNode(0)
        pre = head
        while p and q:
            if p.val <= q.val:
                pre.next = p
                p = p.next
            else:
                pre.next = q
                q = q.next
            pre = pre.next
        if p:
            pre.next = p
        elif q:
            pre.next = q
        return head.next

    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head or not head.next:
            return head
        p, q, p_end = head, head, None
        while q and q.next:
            p_end = p
            p = p.next
            q = q.next.next
        p_end.next = None
        q = self.sortList(p)
        p = self.sortList(head)

        return self.merge(p, q)


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None or head.next == None:
            return head

        left = head
        right = head
        while right.next:
            right = right.next
            if right.next:
                right = right.next
                left = left.next
            else:
                break
        tmp = left.next
        left.next = None
        left = self.sortList(head)
        right = self.sortList(tmp)
        return self.merge(left, right)

    def merge(self, left, right):
        if right == None or left == None:
            return left
        dummy0 = ListNode(0)
        pre = dummy0
        pre.next = left
        dummy = ListNode(0)
        pre2 = dummy
        dummy.next = right

        while left and right:
            if left.val <= right.val:
                pre = left
                left = left.next
            else:
                pre2.next = right.next
                right.next = pre.next
                pre.next = right
                pre = right
                right = pre2.next
        if right:
            pre.next = right
        return dummy0.next

# https://leetcode.com/discuss/15420/java-solution-with-strict-o-1-auxiliary-space-complexity
# https://leetcode.com/discuss/28594/bottom-recurring-with-space-complextity-time-complextity
