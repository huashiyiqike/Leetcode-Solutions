public class Solution {
    public void helper(List<List<Integer>> res, List<Integer> path, int remain, int end, int start){
        if(remain == 0) {
            res.add(new ArrayList<>(path));
            return;
        }
        if(remain <= 0) return;
        for(int i = start; i < end; i++){
            List<Integer> newpath = new ArrayList<Integer>(path);
            newpath.add(i);
            helper(res, newpath, remain-1, end, i+1);
        }
    }
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        helper(res, new ArrayList<>(), k, n+1, 1);
        return res;
    }
}

public class Solution {
    
    Integer[] num;
    Integer[] stack;
    int target;
    
    ArrayList<List<Integer>> found;
    
    
    void search(int p){
        if(p == target){
            found.add(new ArrayList<Integer>(Arrays.asList(stack)));
            return;
        }
        
        for(Integer n : num){
            if(p > 0 && n <= stack[p - 1]) continue;
            
            stack[p] = n;
            search(p + 1);
        }
    }
    
    public List<List<Integer>> combine(int n, int k) {
        
        target = k;
        
        num = new Integer[n];
        for(int i = 1; i <= n; i++) num[i - 1] = i;
        
        stack = new Integer[k];
        
        found = new ArrayList<List<Integer>>();
        
        search(0);
        
        return found;
    }
}
