import java.lang.Object;
import java.lang.Override;
import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>(new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1, ListNode o2) {
                return o1.val - o2.val;
            }
        });
        for(int i = 0; i < lists.length; i++){
            if(lists[i]!=null)  queue.offer(lists[i]);
        }
        ListNode dummy = new ListNode(0), res = dummy;
        while(!queue.isEmpty()){
            ListNode tmp = queue.poll();
            if(tmp.next != null){
                queue.offer(tmp.next);
            }
            res.next = tmp;
            res = res.next;
        }
        return dummy.next;
    }
}
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
import java.util.*;

public class Solution {
    public ListNode merge(ListNode A, ListNode B){
        ListNode dummy = new ListNode(0), cur = dummy;
        while(A != null && B != null){
            if(A.val < B.val) {
                cur.next = A;
                A = A.next;
            }
            else{
                cur.next = B;
                B = B.next;
            }
            cur = cur.next;
        }
        if(A != null){
            cur.next = A;
        }
        else{
            cur.next = B;
        }
        return dummy.next;
    }
    public ListNode mergeKArrayList(List<ListNode> lists){

        final int size = lists.size();

        if(size == 0) return null;
        if(size == 1) return lists.get(0);
        if(size == 2) return merge(lists.get(0), lists.get(1));

        return merge(mergeKArrayList(lists.subList(0, size / 2)),
                mergeKArrayList(lists.subList(size / 2, size)));


    }
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0) return null;
        if(lists.length == 1) return lists[0];
        List<ListNode> list = Arrays.asList(lists);
        return merge(mergeKArrayList(list.subList(0, list.size() / 2)),
                mergeKArrayList(list.subList(list.size()/ 2, list.size())));
//        return merge(mergeKLists((ListNode[]) list.subList(0, list.size() / 2).toArray()),
//                mergeKLists((ListNode[])list.subList(list.size()/2,list.size()).toArray()));
    }
}

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    
    ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode rt = new ListNode(0);
        ListNode h = rt;
        
        while( l1 != null && l2 != null){
            if(l1.val < l2.val){
                rt.next = l1;
                l1 = l1.next;
            }else{ 
                rt.next = l2;
                l2 = l2.next;
            }
            
            rt = rt.next;
        }

        if(l1 != null) rt.next = l1;
        else rt.next = l2;
        
        
        return h.next;
    }
    
    public ListNode mergeKLists(List<ListNode> lists) {
        
        final int size = lists.size();
        
        if(size == 0) return null;
        if(size == 1) return lists.get(0);
        if(size == 2) return mergeTwoLists(lists.get(0), lists.get(1));
        
        return mergeTwoLists(mergeKLists(lists.subList(0, size / 2)), mergeKLists(lists.subList(size / 2, size)));
    }
}
