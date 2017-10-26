 /**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var oddEvenList = function(head) {
    if(!head) {
        return head;
    }
    var even = new ListNode(null);
    var current = head;
    var currentEven = even;
    while (!!current.next) {
        currentEven.next = current.next;
        currentEven = currentEven.next;
        if (!!current.next.next) {
            current.next = current.next.next;
            current = current.next;
            currentEven.next = current.next;
        } else {
            break;
        }
    }
    current.next = even.next;
    return head;
}; 