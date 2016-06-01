/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}[[],[-1,5,11],[],[6,10]]
 */
var mergeKLists = function(lists) {
    if(lists.length == 0){return []}
    else if(lists.length == 1){return lists[0];}
	else if(lists.length == 2){return merge(lists[0], lists[1]);}
	else return merge(
		mergeKLists(
			lists.slice(0, Math.floor( lists.length/2 ) )
		),
		mergeKLists(
			lists.slice(Math.floor( lists.length/2 ) )
		)
		);
};
function merge(p, q){
	var dummy = new ListNode(0), head = dummy;
	while(!!p && !!q){
		if(p.val < q.val){
			head.next = p;
			p = p.next;
			head = head.next;
		}else{
			head.next = q;
			q = q.next;
			head = head.next;
		}
	}
	if(!!p){head.next = p;}
	else{head.next = q;}
	return dummy.next;
}