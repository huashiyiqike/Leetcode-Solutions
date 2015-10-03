/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void reorderList(ListNode head) {
        if(head == null || head.next == null) return;
        ListNode fast = head,slow = head;
        while(fast.next != null){
            fast = fast.next;
            if(fast.next != null) {
                fast = fast.next;
                slow = slow.next;
            }
        }
        ListNode dummy = new ListNode(0);
        dummy.next = slow.next;
        slow.next = null;

        ListNode cur = dummy.next;
        while(cur.next != null){
            ListNode tmp = cur.next.next;
            cur.next.next = dummy.next;
            dummy.next = cur.next;
            cur.next = tmp;
        }

        cur = head;
        while(dummy.next != null){
            ListNode tmp = dummy.next.next;
            dummy.next.next = cur.next;
            cur.next = dummy.next;
            dummy.next = tmp;
            cur = cur.next.next;
        }
    }
}
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void reorderList(ListNode head) {
        if(head == null || head.next == null) return;
        ListNode odd = new ListNode(0);
        ListNode cur = head;
        ListNode tmp;
        int count = 0;
        while(cur.next != null){
            if(count%2 == 0){
                tmp = cur.next.next;
                cur.next.next = odd.next;
                odd.next = cur.next;
                cur.next = tmp;
            }
            cur = cur.next;
            count++;
        }
        cur = head;
        while(odd.next != null){
            tmp = cur.next;
            ListNode tmp2 = odd.next.next;
            odd.next.next = cur.next;
            cur.next = odd.next;
            cur.next.next = tmp;
            cur = tmp;
            odd.next = tmp2;
        }
    }
}

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    
    ListNode reverse(ListNode head){
        ListNode prev = null;
        
        while(head != null){
            ListNode t = head.next;
            
            head.next = prev;
            prev = head;
            
            head = t;
        }
        
        return prev;
    }
    
    ListNode mid(ListNode head){
        
        ListNode fast = head;
        ListNode slow = head;
        
        while(fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        
        return slow;
    }
    
    public void reorderList(ListNode head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(head == null) return;
        if(head.next == null) return;

        ListNode left = head;

        ListNode mid = mid(head);

        ListNode right = mid.next;

        if(right == null) return;

        mid.next = null;

        right = reverse(right);

        while(head != null){
            ListNode t = head.next;

            ListNode r = right;

            if(r == null) return;

            head.next = r;
            right = right.next;
            r.next = t;

            head = t;
        }

    }
}