# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
from collections import defaultdict

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        newlist = RandomListNode(0)


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return head
        dict = {}
        cur = head
        pre = None
        while cur:
            tmp = RandomListNode(cur.label)
            dict[cur] = tmp
            if pre:
                pre.next = tmp
            pre = tmp
            cur = cur.next
        cur = head
        while cur:
            if cur.random:
                dict[cur].random = dict[cur.random]
            cur = cur.next
        return dict[head]

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
from collections import defaultdict


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        dict = {}
        p = head
        count = 0
        res = []
        while p:
            res.append(RandomListNode(p.label))
            dict[p] = count
            p = p.next
            count += 1

        p = head
        for i in range(count):
            if i != count - 1:
                res[i].next = res[i + 1]
            else:
                res[i].next = None
            if p.random:
                res[i].random = res[dict[p.random]]
            p = p.next
        return res[0]


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        dicts = {}
        p = head
        res = RandomListNode(0)
        resfinal = res
        while p:
            res.next = RandomListNode(p.label)
            dicts[p] = res.next
            p = p.next
            res = res.next

        p = head
        res = resfinal.next
        while p:
            if p.random in dicts:
                res.random = dicts[p.random]
            p = p.next
            res = res.next

        return resfinal.next
