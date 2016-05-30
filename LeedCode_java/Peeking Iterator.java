/*
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
*/
public class LRUCache {
    class Node{
        Node pre,next;
        int key;
        int value;
        public Node(int key,int value) {
          this.key=key;
          this.value=value;
       }
        
    }
    HashMap<Integer,Node> map=new HashMap<Integer,Node> ();
    Node head=null;
    Node end=null;
    int capacity;
    public LRUCache(int capacity) {
        this.capacity=capacity;
    }
    
    public int get(int key) {
         if(map.containsKey(key)){
            Node cur=map.get(key);
            remove(cur);
            updata(cur);
            return cur.value;
         }
         return -1;
    }
    public void updata(Node node) {
        node.next=head;
        node.pre=null;
        if(head!=null){
            head.pre=node;
        }
        head=node;
        if(end==null){
            end=head;
        }
    }
    public void remove(Node node) {
        if(node.pre!=null){
              node.pre.next=node.next;
        }else{
          head=node.next;
        }
         if(node.next!=null){
            node.next.pre=node.pre;
        }else{
           
             end=node.pre;
        }
    }
    public void set(int key, int value) {
        if(map.containsKey(key)){
            Node cur=map.get(key);
            cur.value=value;
            remove(cur);
            updata(cur);
        }else{
             Node node=new Node(key,value);
           
             if(map.size()>=capacity){
                 map.remove(end.key);
                 remove(end);
                 updata(node);
             }else{
                 updata(node); 
             }
             map.put(key,node);
        }
    }
}