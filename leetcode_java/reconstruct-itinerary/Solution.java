public class Solution {
    public List<String> findItinerary(String[][] tickets) {
        List<String>  result=new ArrayList<String>();
        if(tickets==null||tickets.length==0){
            return result;
        }
        Map<String, ArrayList<String>> graph=new HashMap<String, ArrayList<String>>();
        for(String[] tick:tickets){
            if(!graph.containsKey(tick[0])){
                graph.put(tick[0],new ArrayList<String>());
            }
             graph.get(tick[0]).add(tick[1]);
        }
        for(ArrayList<String> a : graph.values()){
            Collections.sort(a);
        }
        Stack<String> stack=new Stack<String>();
        stack.add("JFK");
        while(!stack.isEmpty()){
            while((graph.containsKey(stack.peek()))&&(!(graph.get(stack.peek()).isEmpty()))){
                stack.push(graph.get(stack.peek()).remove(0));
            }
            result.add(0,stack.pop());
        }
        return result;
    }
}