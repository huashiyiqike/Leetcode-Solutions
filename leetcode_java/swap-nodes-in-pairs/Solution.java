/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy, cur = dummy.next;
        while(cur != null && cur.next != null){
            ListNode tmp = cur.next;
            pre.next = cur.next;
            cur.next = cur.next.next;
            tmp.next = cur;
            pre = cur;
            cur = cur.next;
        }
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
    public ListNode swapPairs(ListNode head) {
        
        
        if (head == null) return null;
        
        if (head.next == null) return head;
        
        ListNode newhead = head.next;
        head.next = swapPairs(head.next.next);
        
        newhead.next = head;
        
        return newhead;
        
    }
}