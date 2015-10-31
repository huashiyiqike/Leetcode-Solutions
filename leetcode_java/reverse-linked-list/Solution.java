/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) { val = x; }
 * }
 */

public class Solution {
    ListNode newhead;

    public ListNode helper(ListNode head) {
        if (head.next == null) {
            newhead = head;
            return head;
        }
        ListNode tail = helper(head.next);
        tail.next = head;
        return head;
    }

    public ListNode reverseList(ListNode head) {
        if (head == null) return head;
        helper(head).next = null;
        return newhead;
    }
}

public class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode cur = head;
        while (cur.next != null) {
            ListNode tmp = cur.next.next;
            cur.next.next = dummy.next;
            dummy.next = cur.next;
            cur.next = tmp;
        }
        return dummy.next;
    }
}

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {

        if (head == null) return null;
        if (head.next == null) return head;

        ListNode tail = head.next;
        ListNode reversed = reverseList(head.next);

        tail.next = head;

        head.next = null;

        return reversed;
    }
}
