public class Solution {
    public void helper(List<List<Integer>> res, List<Integer> path, int[] candidates, int target, int start){
        if(target == 0) res.add(new ArrayList<>(path));
        for(int i = start; i < candidates.length; i++){
            int tmp = target - candidates[i];
            if(tmp < 0) continue;
            List<Integer> newpath = new ArrayList<Integer>(path);
            newpath.add(candidates[i]);
            helper(res, newpath, candidates, target - candidates[i], i);
        }
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(candidates);
        helper(res, new ArrayList<>(), candidates, target, 0);
        return res;
    }
}
public class Solution {
    int target;
    
    int[] candidates;
    
    int[] stack;
    
    ArrayList<List<Integer>> rt;
    
    void search(int sp, int cur){

        if(cur == target){
            ArrayList<Integer> found = new ArrayList<Integer>();
            for(int i = 0; i < stack.length; i++){
                for(int j = 0; j < stack[i]; j++){
                    found.add(candidates[i]);
                }
            }
            
            rt.add(found);
            return;
            
        }
        
        if(sp >= stack.length){
            return;
        }
        
        int toadd = candidates[sp];
        
        for(int i = 0; cur + toadd * i <= target; i++ ){
            stack[sp] = i;
            search(sp + 1, cur + toadd * i);
            stack[sp] = 0;
        }
        
    }
 
 
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        
        this.target = target;
        
        this.candidates = candidates;
        
        stack = new int[candidates.length];
        
        rt = new ArrayList<List<Integer>>();
        
        search(0, 0);
        
        return rt;
        
    }
}
