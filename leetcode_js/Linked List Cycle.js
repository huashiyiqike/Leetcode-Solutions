var hasCycle = function(head){
    var slow = head;
    while(head !== null && head.next !== null){
        head = head.next.next;
        slow = slow.next;
        if(head === slow) return true;
    }
    return false;
}