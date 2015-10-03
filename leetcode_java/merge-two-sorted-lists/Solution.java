/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null) return l2;
        else if(l2 == null) return l1;
        ListNode dummy = new ListNode(0), cur1 = new ListNode(1),
                cur2 = new ListNode(2), cur = dummy;
        cur1.next = l1; // sigh, no link deletion, no need for dummy
        cur2.next = l2;
        while(cur1.next != null && cur2.next != null){
            if(cur1.next.val < cur2.next.val){
                cur.next = cur1.next;
                cur1.next = cur1.next.next;
            }
            else{
                cur.next = cur2.next;
                cur2.next = cur2.next.next;
            }
            cur = cur.next;
        }
        if(cur1.next != null){
            cur.next = cur1.next;
        }
        if(cur2.next != null){
            cur.next = cur2.next;
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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        ListNode rt = new ListNode(0);
        ListNode h = rt;
        
        while( l1 != null && l2 != null){
            if(l1.val < l2.val){
                rt.next = l1;
                l1 = l1.next;
            }else{ 
                rt.next = l2;
                l2 = l2.next;
            }
            
            rt = rt.next;
        }

        if(l1 != null) rt.next = l1;
        else rt.next = l2;
        
        
        return h.next;

        
    }
}