/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
	if(n == 0) return head;
	var dummy = new ListNode(0);
	dummy.next = head;
    var ahead = cur = dummy;
    while(n-- >0){ahead = ahead.next;}
    while(ahead.next != null){
    	ahead = ahead.next;
    	cur = cur.next;
    }
    cur.next = cur.next.next;
    return dummy.next;
};