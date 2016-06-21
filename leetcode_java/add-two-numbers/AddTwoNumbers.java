/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode p = l1 , q = l2 , temp = null , pre = null;
        int c = 0;
        int sum ;
        while(p != null && q != null){
            sum = p.val + q.val + c;
            c =  sum / 10;
            p.val = sum % 10;
            pre = p;
            p = p.next ;
            q = q.next;
        }
        if(p == null){
            pre.next =  q ;
        }
        temp = pre.next ;
        if(temp == null && c > 0){
             ListNode newNode = new ListNode(c);
             newNode.next = null;
            pre.next =  newNode;
        }
        while(temp != null && temp.next != null){
            temp.val = temp.val + c;
            c= temp.val / 10;
            temp.val = temp.val % 10;
            temp = temp.next;
        }
        int val = 0;
        if(temp != null){
            val = temp.val+c;
            temp.val =  val % 10 ;
            c= val / 10;
            
           
        }
        if(temp != null && c >0 ){
            ListNode node = new ListNode(c );
            node.next = null;
            temp.next = node;
            
        }
        
        return l1;
       
    }