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
var addTwoNumbers = function(l1, l2) {
    var inc = 0, res = l1, pre1 = l1, pre2 = l2;
    while(l1 !== null && l2 !== null){
        l1.val += l2.val + inc;
        inc = Math.floor(l1.val/10);
        l1.val %= 10;
        pre1 = l1, pre2 = l2;
        l1 = l1.next;
        l2 = l2.next;
    }
    if(l1 === null){
        pre1.next = l2;
        while(l2 !== null){
            l2.val += inc;
            inc = Math.floor(l2.val/10);
            l2.val %= 10;
            pre2 = l2;
            l2 = l2.next;
        }
        if(inc > 0) pre2.next = new ListNode(1);
    }
    else if(l2 === null){
        while(l1 !== null){
            l1.val += inc;
            inc = Math.floor(l1.val/10);
            l1.val %= 10;
            pre1 = l1;
            l1 = l1.next;
        }
        if(inc > 0) pre1.next = new ListNode(1);
    }
    else if(inc >0) pre1.next = new ListNode(1);
    return res;
};