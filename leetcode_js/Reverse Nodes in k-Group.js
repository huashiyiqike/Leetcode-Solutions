//25. Reverse Nodes in k-Group My Submissions Question
//Total Accepted: 51020 Total Submissions: 191876 Difficulty: Hard
//Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
//
//If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
//
//You may not alter the values in the nodes, only nodes itself may be changed.
//
//Only constant memory is allowed.
//
//For example,
//Given this linked list: 1->2->3->4->5
//
//For k = 2, you should return: 2->1->4->3->5
//
//For k = 3, you should return: 3->2->1->4->5
//

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
function ListNode(val) {
    this.val = val;
    this.next = null;
}
var reverseList = function (res, k) {
    var cur = res.next
    for (var i = 0; i < k - 1; i++) {
        next = cur.next
        cur.next = next.next
        next.next = res.next
        res.next = next
    }
    return cur;
}
var reverseKGroup = function (head, k) {
    var pre = new ListNode(0),
        res = pre;
    pre.next = head;
    while (true) {
        var next = pre;
        for (var i = 0; i < k; i++) {
            if (next.next !== null) next = next.next;
            else return res.next;
        }
        pre = reverseList(pre, k);
    }
}
var tmphead = new ListNode(1);
tmphead.next = new ListNode(2);
document.writeln(reverseKGroup(tmphead, 2));