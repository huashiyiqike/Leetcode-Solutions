# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        m = ListNode(0)
        res = m
        n = ListNode(0)
        tmp = n
        while head:
            if head.val < x:
                m.next = head
                m = m.next
            else:
                n.next = head
                n = n.next
            head = head.next
        n.next = None
        m.next = tmp.next
        return res.next


if __name__ == "__main__":
    a = ListNode(2)
    b = ListNode(1)
    a.next = b
    m = Solution()
    l = m.partition(a, 2)
    print l.val
    print l.next.val
