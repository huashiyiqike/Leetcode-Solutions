/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
function ListNode(val) {
      this.val = val;
      this.next = null;
 }
/**
 * @param {ListNode} head
 * @return {ListNode}
 */ 
var reverseList = function(head) {
    var res = new ListNode(0);
    res.next = head;
    if(head === null) return head;
    var pre = head;
    while(pre.next !== null){
        var tmpnext = pre.next.next;
        pre.next.next = res.next;
        res.next = pre.next;
        pre.next = tmpnext;
    }
    return res.next;
};
document.writeln(reverseList(new ListNode(1)))