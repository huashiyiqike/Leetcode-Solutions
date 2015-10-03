# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# no stack, in place change connection
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m==n:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        for i in range(m-1):
            pre=pre.next
        tail=pre.next

        for i in range(n-m):
            x=pre.next
            pre.next=tail.next
            tail.next=tail.next.next
            pre.next.next=x
        return dummy.next


# same as 8.2
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m==n:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        for i in range(m):
            end=p
            p=p.next

        q=p.next
        for i in range(n-m): # first reverse the part
            tmp=q.next
            q.next=p
            p=q
            q=tmp
        end.next.next=q # then connect
        end.next=p
        return dummy.next

#反转的方法就是每读到一个结点，把它插入到m结点前面位置，然后m结点接到读到结点的下一个
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m==n:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        for i in range(m-1):
            pre=pre.next
        tmp=pre.next

        for i in range(n-m):
            x=pre.next
            pre.next=tmp.next
            tmp.next=tmp.next.next
            pre.next.next=x
        return dummy.next

# This is not in-place
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m==n:
            return head
        l1=head
        stacks=[]
        for i in range(m-1):
            l1=l1.next
        l2=l1
        for i in range(n-m+1):
            stacks.append(l2.val)
            #print l2.val
            l2=l2.next
        for i in range(n-m+1):
            l1.val=stacks.pop()
            l1=l1.next
        return head

if __name__=="__main__":
    a=Solution()
    m=ListNode(1)
    n=ListNode(2)
    p=ListNode(3)
    m.next=n
    n.next=p
    l=a.reverseBetween(m,1,3)
    print l.val
    print l.next.val
    print l.next.next.val
     