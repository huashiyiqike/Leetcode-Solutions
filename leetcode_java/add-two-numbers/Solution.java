/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
import java.util.*;
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2){
        ListNode dummy = new ListNode(0), cur = dummy;
        int carry = 0;
        while(l1 != null && l2 != null){
            int total = l1.val+l2.val+carry;
            ListNode tmp = new ListNode(total%10);
            cur.next = tmp;
            cur = cur.next;
            carry = total/10;
            l1 = l1.next;
            l2 = l2.next;
        }
        while(l1 != null){
            int total = l1.val+carry;
            ListNode tmp = new ListNode(total%10);
            cur.next = tmp;
            cur = cur.next;
            carry = total/10;
            l1 = l1.next;
        }
        while(l2 != null){
            int total = l2.val+carry;
            ListNode tmp = new ListNode(total%10);
            cur.next = tmp;
            cur = cur.next;
            carry = total/10;
            l2 = l2.next;
        }
        if(carry != 0)
            cur.next = new ListNode(carry);
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        ListNode r = new ListNode(0);
        ListNode h = r;
        ListNode beforeend = r;
        
        while(l1 !=null && l2 != null){
            r.val += l1.val + l2.val;
            
            r.next = new ListNode(r.val / 10);
            r.val %= 10;
            
            beforeend = r;
            r = r.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        
        ListNode rest;
        if (l1 == null) rest = l2; else rest = l1;
        
        while(rest != null){
            r.val += rest.val;
            
            r.next = new ListNode(r.val / 10);
            r.val %= 10;
            
            beforeend = r;
            r = r.next;
            rest = rest.next;
        }
        
        if(beforeend.next != null && beforeend.next.val == 0) beforeend.next = null;
        
        return h;
    }
}