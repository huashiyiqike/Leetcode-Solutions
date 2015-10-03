/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode cur = dummy;
        int i = 0;
        for(; i < m-1; i++){
            cur = cur.next;
        }
        ListNode pre = cur;
        cur = cur.next;
        for(;i<n-1;i++){
            ListNode tmp = cur.next.next;
            cur.next.next = pre.next;
            pre.next = cur.next;
            cur.next = tmp;
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
    public ListNode reverseBetween(ListNode head, int m, int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        
        if(head == null) return null;
        if(head.next == null) return head;
        
        int c = 1;
        
        final ListNode _head = head;
        
        ListNode prev = null;
        
        ListNode jointLeft = null;
        ListNode jointRight = null;
        
        while(head != null){
            
            ListNode t = head.next; 
            
            if(c == m){
                jointLeft  = prev;
                jointRight = head;
            }
            
            if(c >= m && c <= n){
                head.next = prev;
            }
            
            prev = head;
            head = t;
            
            if(c == n){
                if(jointLeft != null){
                    jointLeft.next = prev;
                }
                jointRight.next = head;
                
                if(jointRight == _head){
                    return prev;
                }else{
                    return _head;
                }
            }
            
            c++;
            
        }
        
        return _head;
    }
}