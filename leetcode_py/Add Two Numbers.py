# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode(-1)
        head=dummy
        carry=0

        while l1 or l2:
            tmpres=0
            if l1:
                tmpres+=l1.val
                l1=l1.next
            if l2:
                tmpres+=l2.val
                l2=l2.next
            tmpres+=carry
            carry=tmpres/10
            tmpres%=10
            head.next=ListNode(tmpres)
            head=head.next
        if carry:
            head.next=ListNode(carry)
        return dummy.next
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def moretoend(self,new,up):
        while new.next is not None:
            new.val=new.val+up
            up=new.val/10
            new.val%=10
            new=new.next

        new.val=new.val+up
        up=new.val/10
        new.val%=10
        if up>0:
            new.next=ListNode(up)


    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        up=0
        if l1==None:
            return l2
        if l2==None:
            return l1
        head=l1
        while l1.next is not None and l2.next is not None:
            l1.val=l1.val+l2.val+up
            up=l1.val/10
            l1.val%=10
            l1=l1.next
            l2=l2.next

        if l2.next is None and l1.next is None:
            l1.val+=l2.val+up
            up=l1.val/10
            l1.val%=10
            if up>0:
                l1.next=ListNode(up)
        elif l2.next is None:
            l1.val+=l2.val
            self.moretoend(l1,up)
        elif l1.next is None:
            l1.val+=l2.val
            l1.next=l2.next
            self.moretoend(l1,up)

        return head
