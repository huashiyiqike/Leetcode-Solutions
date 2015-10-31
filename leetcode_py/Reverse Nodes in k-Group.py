# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, p1, k):
        cur = p1.next
        for i in range(k - 1):
            next = cur.next
            cur.next = next.next
            next.next = p1.next  # notice not cur!
            p1.next = next
        return cur

    def testkgroup(self, start_pre, k):
        for i in range(k):
            start_pre = start_pre.next
            if not start_pre:
                return False
        return True

    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if head == None or head.next == None or k <= 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        while self.testkgroup(p1, k):
            p1 = self.reverse(p1, k)
        return dummy.next


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        list = head
        if list == None or k <= 1 or list.next == None:
            return list
        dummy = ListNode(0)
        stack = []
        pre = dummy
        p = head
        dummy.next = head

        while p is not None:
            for i in range(k):
                stack.append(p)
                p = p.next
                if p == None:
                    break

            if len(stack) == k:
                for i in range(k):
                    pre.next = stack.pop()
                    pre = pre.next
            else:
                for i in range(len(stack)):
                    pre.next = stack[i]
                    pre = pre.next

        pre.next = None
        return dummy.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    a = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    tmp = a.reverseKGroup(head, 2)
    while tmp:
        print tmp.val
        tmp = tmp.next
