public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        UndirectedGraphNode result = null;
        if(node == null){
            return result;
        }
        Stack<UndirectedGraphNode> stack = new Stack<UndirectedGraphNode>();
        stack.push(node);
        List<Integer> list = new ArrayList<Integer>();
        HashMap<Integer,UndirectedGraphNode> map = new HashMap<Integer,UndirectedGraphNode>();
        UndirectedGraphNode front;
        while(!stack.empty()){
            front = stack.peek();
            stack.pop();
            if((front == null)||(list.contains(front.label))){
                continue;
            }
            list.add(front.label);
            if(!map.containsKey(front.label)){
                map.put(front.label,new UndirectedGraphNode(front.label));
            }
            if(result == null){
                result = new UndirectedGraphNode(front.label);
            }
            List<UndirectedGraphNode> neighbor = front.neighbors;
            for(UndirectedGraphNode nei:neighbor){
                stack.push(nei);
                if(!map.containsKey(nei.label)){
                    map.put(nei.label, new UndirectedGraphNode(nei.label));
                    
                }
                 map.get(front.label).neighbors.add(map.get(nei.label));
            }
        }
        return map.get(result.label);
    }
}