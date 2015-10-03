# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, p):
        dummy = ListNode(0)
        dummy.next = p
        cur = p
        while cur.next:
            tmp = cur.next.next
            cur.next.next = dummy.next
            dummy.next = cur.next
            cur.next = tmp
        return dummy.next

    def helper(self, p1, p2):
        p1 = self.reverse(p1)
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        if p1 or p2:
            return False
        return True

    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        count = 0
        p = head
        while p:
            p = p.next
            count += 1
        p = head
        for i in range(count/2 - 1):
            p = p.next
        if count%2 == 0:
            head2 = p.next
            p.next = None
            return self.helper(head, head2)
        else:
            head2 = ListNode(p.next.val)
            head2.next = p.next.next
            p.next.next = None
            return self.helper(head, head2)
