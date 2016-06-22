/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode oddEvenList(ListNode head) {
        ListNode top = null;
        if(head == null){
            return null;
        }
        if(head.next == null){
            return head;
        }
        ListNode p = head ,temp = null ,q = head.next ,pre = q;
        while(q != null && q.next != null){
            p.next = q.next ;
            p = p.next;
            q.next = p.next;
            q = q.next;
        }
        p.next = pre;
        return head;
    }
}