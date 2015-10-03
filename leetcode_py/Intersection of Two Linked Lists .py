# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        p = headA
        q = headB
        while p or q:
            if not p:
                p = headB
            if not q:
                q = headA
            if p == q:
                return p
            p = p.next
            q = q.next
        return None


class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA==None or headB==None:
            return None
            
        tmpA=headA
        tmpB=headB
        countA=0
        countB=0
        
        while tmpA.next!=None:
            countA+=1
            tmpA=tmpA.next
        while tmpB.next!=None:
            countB+=1
            tmpB=tmpB.next
            
        if tmpA!=tmpB:
            return None
            
        tmpA=headA
        tmpB=headB
        if countA>countB:
            for i in range(countA-countB):
                tmpA=tmpA.next
        elif countB>countA:
            for i in range(countB-countA):
                tmpB=tmpB.next
                
        while tmpA!=tmpB:
            tmpA=tmpA.next
            tmpB=tmpB.next
        return tmpA
