/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    ListNode reverse(ListNode head){
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        while(head.next != null){
            ListNode tmp = head.next.next;
            head.next.next = dummy.next;
            dummy.next = head.next;
            head.next = tmp;
        }
        return dummy.next;
    }
    public boolean isPalindrome(ListNode head) {
        int len = 0;
        ListNode cur = head;
        while(cur != null){
            cur = cur.next;
            len++;
        }
        if(len <= 1) return true;
        cur = head;
        for(int i = 0; i < len/2 - 1; i++){
            cur = cur.next;
        }
        ListNode head2 = reverse(cur.next);
        cur = head;
        while(head2 != null){
            if(head2.val != cur.val) return false;
            head2 = head2.next;
            cur = cur.next;
        }
        return true;
    }
}