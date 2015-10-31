# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = head
        while pre.next:
            if pre.next.val < pre.val:
                res = dummy
                while res.next.val < pre.next.val:  # at least one equal, no need compare with None
                    res = res.next

                tmp = pre.next.next
                pre.next.next = res.next
                res.next = pre.next
                pre.next = tmp
            else:
                pre = pre.next

        return dummy.next


if __name__ == "__main__":
    a = Solution()
    m = ListNode(3)
    n = ListNode(2)
    p = ListNode(4)
    m.next = n
    n.next = p
    m = a.insertionSortList(m)
    print m.val
    print m.next.val
    print m.next.next.val

    m = ListNode(3)
    n = ListNode(1)
    p = ListNode(-1)
    m.next = n
    n.next = p
    m = a.insertionSortList(m)
    print m.val
    print m.next.val
    print m.next.next.val

    a.insertionSortList(p)
    print p.val

# TLE
class Solution:
    def helper(self, res, other):
        if not other:
            return

        tmphead = res
        tmp = other
        other = other.next
        while res.next and res.next.val < tmp.val:
            res = res.next

        tmp.next = res.next
        res.next = tmp

        self.helper(tmphead, other)

    def insertionSortList(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        self.helper(dummy, head)
        return dummy.next
