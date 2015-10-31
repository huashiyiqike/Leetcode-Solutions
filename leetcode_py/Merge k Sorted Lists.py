# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class Solution:
    def merge(self, l1, l2):
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next

    # @param {ListNode[]} lists
    # @return {ListNode}

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return []
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.merge(lists[0], lists[1])
        return self.merge(self.mergeKLists(lists[:len(lists) / 2]), self.mergeKLists(lists[len(lists) / 2:]))


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import heapq


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i]))
        dummy = ListNode(0)
        head = dummy
        if len(heap) > 0:
            tmp = heapq.heappop(heap)
        else:
            return None

        while tmp:
            head.next = tmp[1]
            head = head.next
            if tmp[1].next:
                heapq.heappush(heap, (tmp[1].next.val, tmp[1].next))
            if len(heap) > 0:
                tmp = heapq.heappop(heap)
            else:
                break
        return dummy.next

# in place merge sort http://www.cnblogs.com/daniagger/archive/2012/07/25/2608373.html

# # just sort  https://leetcode.com/discuss/28722/python-133ms-solution   
# from operator import attrgetter
# 
# class Solution:
#     # @param a list of ListNode
#     # @return a ListNode
#     def mergeKLists(self, lists):
#         sorted_list = []
#         for head in lists:
#             curr = head
#             while curr is not None:
#                 sorted_list.append(curr)
#                 curr = curr.next
# 
#         sorted_list = sorted(sorted_list, key=attrgetter('val'))
#         for i, node in enumerate(sorted_list):
#             try:
#                 node.next = sorted_list[i + 1]
#             except:
#                 node.next = None
# 
#         if sorted_list:
#             return sorted_list[0]
#         else:
#             return None

if __name__ == "__main__":
    a = Solution()
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(2)
    a1.next = a2
    a2.next = a3
    b1 = ListNode(1)
    b2 = ListNode(1)
    b3 = ListNode(2)
    b1.next = b2
    b2.next = b3
    tmp = a.mergeKLists([a1, b1])

    while tmp:
        print tmp.val
        tmp = tmp.next
