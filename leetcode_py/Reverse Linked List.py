# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next:
            tmp = cur.next.next
            cur.next.next = dummy.next
            dummy.next = cur.next
            cur.next = tmp
        return dummy.next


class Solution:
    def helper(self, head):
        if not head.next:
            self.head = head
            return head
        tail = self.helper(head.next)
        tail.next = head
        head.next = None
        return head

    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head or not head.next:
            return head
        self.head = None
        self.helper(head)
        return self.head



class Solution:
    def f(self,head):
        if head.next==None:
            self.first=head
            return head 
        else:
            tail=self.f(head.next)
            tail.next=head
            return head 
        
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head ==None:
            return None
        self.first=None
        self.f(head).next=None
        return self.first
    
if __name__=="__main__":
    a=Solution()
    p=ListNode(1)
    q=ListNode(2)
    p.next=q
    print a.reverseList(p).val
#

class Solution:
    def f(self,head):
        if head.next==None:
            self.head=head
            return head
        else:
            tmp=self.f(head.next)
            head.next=None
            tmp.next=head
            return head
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head==None or head.next==None:
            return head
        self.head=None
        self.f(head)
        return self.head


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head ==None:
            return None
        pre,p=None,head
        while p:
            tmp=p.next
            p.next=pre
            pre=p
            p=tmp
        return pre

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head ==None:
            return None
        pre,p=head,head.next
        while p:
            tmp=p
            p=p.next
            tmp.next=pre
            pre=tmp 
        head.next=None
        return pre