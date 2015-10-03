import java.util.*;
class RandomListNode {
         int label;
         RandomListNode next, random;
         RandomListNode(int x) { this.label = x; }
};
/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        Map<RandomListNode, RandomListNode> map = new HashMap<>();
        RandomListNode cur = head, pre = null;
        while(cur != null){
            RandomListNode tmp = new RandomListNode(cur.label);
            map.put(cur, tmp);
            if(pre != null) pre.next = tmp;
            pre = tmp;
            cur = cur.next;
        }
        cur = head;
        while(cur != null){
            map.get(cur).random = map.get(cur.random);
            cur = cur.next;
        }
        return map.get(head);
    }
}
/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        if(head == null) return null;
        
        HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
        
        RandomListNode iter = head;
        while(iter != null){
            RandomListNode born = new RandomListNode(iter.label);
            map.put(iter, born);
            
            iter = iter.next;
        }
        
        iter = head;
        
        while(iter != null){
            RandomListNode islet = map.get(iter);
            
            islet.next = map.get(iter.next);
            islet.random = map.get(iter.random);
            
            iter = iter.next;
        }
        
        return map.get(head);
    }
}