/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    var dummy = new ListNode(0), head = dummy;
    while(!!l1 && !!l2){
    	if(l1.val < l2.val){
    		head.next = l1;
    		head = head.next;
    		l1 = l1.next;
    	}else{
    		head.next = l2;
    		head = head.next;
    		l2 = l2.next;
    	}
    }
    if(!!l1){head.next = l1;}
    else{head.next = l2;}
    return dummy.next
};