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
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if head==None or k==0:
            return head

        p=head
        length=0
        while p:
            p=p.next
            length+=1
        k%=length
        k=length-k
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        for i in range(k):
            p=p.next
        tmp=p
        while tmp.next:
            tmp=tmp.next
        tmp.next=dummy.next
        dummy.next=p.next
        p.next=None
        return dummy.next


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head==None or k==0:
            return head
        
        count=0  
        p1=head
        while p1!=None:
            count+=1
            p1=p1.next
        k%=count    
        p1,p2,count=head,head,0
        
        
        while p1.next!=None and count<k:
            p1=p1.next
            count+=1
        if count<k:
            return head
        while p1.next!=None:
            p1,p2=p1.next,p2.next
        if p1.next==None:
            p1.next=head
            head=p2.next
            p2.next=None
        return head
        
