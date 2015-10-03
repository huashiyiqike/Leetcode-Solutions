# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummy=ListNode(0) 
        head=dummy 
        while l1 and l2:
            if l1.val<l2.val:
                head.next=l1
                head=head.next
                l1=l1.next 
            else:
                head.next=l2
                head=head.next 
                l2=l2.next 
        if l1:
            head.next=l1 
        if l2:
            head.next=l2 
        return dummy.next

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1==None and l2==None:
            return None
        elif l1==None:
            return l2
        elif l2==None:
            return l1

        if l1.val<l2.val:
            tmp=self.mergeTwoLists(l1.next,l2)
            l1.next=tmp
            return l1
        else:
            tmp=self.mergeTwoLists(l1,l2.next)
            l2.next=tmp
            return l2
