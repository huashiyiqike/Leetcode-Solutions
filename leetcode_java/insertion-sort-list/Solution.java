/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution{
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode result = new ListNode(0);
        while(dummy.next != null){
            ListNode res = result;
            while(res.next != null && res.next.val < dummy.next.val){
                res = res.next;
            }
            ListNode tmp = dummy.next.next;
            dummy.next.next = res.next;
            res.next = dummy.next;
            dummy.next = tmp;
        }

        return result.next;
    }
}

// not insertion sort
public class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode resdummy = new ListNode(0);
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode cur = head;
        while(cur != null){
            dummy.next = cur.next;

            ListNode tmppre = resdummy, tmp = resdummy.next;
            while(tmp != null && tmp.val < cur.val){
                tmppre = tmp;
                tmp = tmp.next;
            }
            cur.next = tmppre.next;
            tmppre.next = cur;

            cur = dummy.next;
        }
        return resdummy.next;
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
    public ListNode insertionSortList(ListNode head) {
        
        if(head == null) return null;
        if(head.next == null) return head;
        
        final ListNode _head = new ListNode(Integer.MIN_VALUE);
        _head.next = head;
        
        head = head.next;
        _head.next.next = null;
        
        next:
        while(head != null){
            
            ListNode taken = head;
            head = head.next;
            
            
            ListNode cur = _head.next;
            ListNode last = _head;
            
            
            while(cur != null){
                
                if(cur.val > taken.val){
                    // insert
                    last.next = taken;
                    taken.next = cur;
                    
                    continue next;
                    
                }
                
                cur  = cur.next;
                last = last.next;
            }
            
            last.next = taken;
            taken.next = null;

        }
        
        
        return _head.next;
        
    }
}