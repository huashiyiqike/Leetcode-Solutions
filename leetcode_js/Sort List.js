//148. Sort List My Submissions Question
//Total Accepted: 61309 Total Submissions: 258737 Difficulty: Medium
//Sort a linked list in O(n log n) time using constant space complexity.
//
function ListNode(val) {
      this.val = val;
      this.next = null;
 }
function merge(p, q){
    var head = new ListNode(0), pidx = 0 , qidx = 0, tmphead = head;
    while(p && q){
        if(p.val <= q.val){
            head.next = p;
            p = p.next;
        }else{
            head.next = q;
            q = q.next;
        }
        head = head.next;
    }
    while(p){
        head.next = p;
        p = p.next;
        head = head.next;
    }
    while(q){
        head.next = q;
        q = q.next;
        head = head.next
    }
    return tmphead.next;
}
var sortList = function(head) {
    if(!head || !head.next) return head;
    var p1 = head, p2 = p1.next;
    while(p2.next && p2.next.next){
        p1 = p1.next;
        p2 = p2.next.next;
    } 
    p2 = sortList(p1.next);
    p1.next = null;
    p1 = sortList(head);  
    return merge(p1,p2);
};
hh = new ListNode(3);
hh.next = new ListNode(2);
hh.next.next = new ListNode(4);
var tmp = sortList(hh);
while(tmp){
document.write(tmp.val);
tmp = tmp.next;
}