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
var swapPairs = function(head) {
    var pre = new ListNode(0);
    pre.next = head;
    while(pre.next !== null && pre.next.next !== null){
        var tmp = pre.next.next.val;
        pre.next.next.val = pre.next.val;
        pre.next.val = tmp;
        pre = pre.next.next;
    }
    return head;
}