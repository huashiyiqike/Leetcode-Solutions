/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null) return head;
        ListNode cur = head;
        while(cur.next != null){
            if(cur.next.val == cur.val) cur.next = cur.next.next;
            else cur = cur.next;
        }
        return head;
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
    public ListNode deleteDuplicates(ListNode head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(head == null) return null;
        if(head.next == null) return head;
        
        int v = head.val;
        
        ListNode node = head.next;
        ListNode lasthead = head;
        while(node != null){
            
            while(node != null && node.val == lasthead.val) node = node.next;

            lasthead.next = node;
            lasthead = node;
            
            if(node != null) node = node.next;
            
        }
        
        return head;
    }
}