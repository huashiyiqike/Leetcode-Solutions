/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode large = new ListNode(0), dummy = new ListNode(0), largecur = large;
        dummy.next = head;
        ListNode cur = dummy;
        for(;cur.next != null;){
            if(cur.next.val >= x){
                largecur.next = cur.next;
                cur.next = cur.next.next;
                largecur = largecur.next;
                largecur.next = null;
            }
            else{
                cur = cur.next;
            }
        }
        cur.next = large.next;
        return dummy.next;
    }
}

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode partition(ListNode head, int x) {
        if(head == null) return null;
        if(head.next == null) return head;
        
        final ListNode less = new ListNode(0);
        final ListNode greater = new ListNode(0);
        
        ListNode _less    = less;
        ListNode _greater = greater;
        
        while(head != null){
            ListNode t = head;
            head = head.next;
            
            if(t.val < x){
                _less.next = t;
                _less = _less.next;
            }else {
                _greater.next = t;
                _greater = _greater.next;
            }
        }
        
        _greater.next = null;
        
        _less.next  = greater.next;
        
        return less.next;
        
    }
}
