public class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Integer> result = new ArrayList<Integer>();
        if(n< = 0){
            return result;
        }
        if(n == 1&&( edges == null || edges.length == 0)){
            result.add(0);
            return result;
        }
        List<Set<Integer>> set = new ArrayList<>();
        for(int i = 0;i < n;i++){
            set.add(new HashSet());
        }
        for(int[] edge:edges){
            int start = edge[0];
            int end = edge[1];
            set.get(start).add(end);
            set.get(end).add(start);
        }
        List<Integer> leaf = new ArrayList<Integer>();
        for(int i = 0; i < n;i++){
            if(set.get(i).size()==1){
                leaf.add(i);
            }
        }
        while(n>2){
            List<Integer> newLeaf = new ArrayList<Integer>();
            int size = leaf.size();
            n = n-size;
            for(int i = 0;i < size; i++){
                int next = leaf.get(i);
                int setNext = set.get(next).iterator().next();
                 set.get(setNext).remove(next);
                if(set.get(setNext).size() == 1){
                    newLeaf.add(setNext);
                }
            }
            leaf = newLeaf;
        }
        return leaf;
    }
}