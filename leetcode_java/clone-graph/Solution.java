import com.sun.javafx.collections.MappingChange;

import java.util.ConcurrentModificationException;
import java.util.HashMap;
import java.util.LinkedList;

/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if(node == null) return null;
        HashMap<UndirectedGraphNode, UndirectedGraphNode> m = new HashMap<>();
        UndirectedGraphNode start = new UndirectedGraphNode(node.label);
        m.put(node, start);
        LinkedList<UndirectedGraphNode> s = new LinkedList<>();
        s.push(node);
        while(!s.isEmpty()){
            UndirectedGraphNode current = s.pop();
            for(UndirectedGraphNode c:current.neighbors){
                if(!m.containsKey(c)){
                    UndirectedGraphNode tmp = new UndirectedGraphNode(c.label);
                    s.push(c);
                    m.put(c, tmp);
                }
                m.get(current).neighbors.add(m.get(c));
            }
        }
        return start;
    }
}
/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        
        if(node == null) return null;
        
        // visit
        HashMap<UndirectedGraphNode, UndirectedGraphNode> clone = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
        
        Deque<UndirectedGraphNode> queue = new LinkedList<UndirectedGraphNode>();
        
        queue.add(node);
        
        while(queue.size() > 0){
            
            UndirectedGraphNode n = queue.poll();
            if(!clone.containsKey(n)){
                clone.put(n, new UndirectedGraphNode(n.label));
                
                for(UndirectedGraphNode neighbor : n.neighbors){
                    queue.add(neighbor);
                }
            }
        }
        
        queue.add(node);
        HashSet<UndirectedGraphNode> visit = new HashSet<UndirectedGraphNode>();
        
        while(queue.size() > 0){
            
            UndirectedGraphNode n = queue.poll();
            if(!visit.contains(n)){
                visit.add(n);
                
                UndirectedGraphNode c = clone.get(n);
                
                for(UndirectedGraphNode neighbor : n.neighbors){
                    c.neighbors.add(clone.get(neighbor));
                    queue.add(neighbor);
                }
            }
        }
        
        return clone.get(node);
        
    }
}