var detectCycle = function(head) {
    var slow = head, fast = head;
    while(fast !== null && fast.next !== null){
        fast = fast.next.next;
        slow = slow.next;
        if(fast === slow){
            fast = head;
            while(fast !== slow){
                fast = fast.next;
                slow = slow.next;
            }
            return fast;
        }
    }
    return null;
}