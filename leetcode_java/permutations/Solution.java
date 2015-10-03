public class Solution {
    public void helper(List<List<Integer>> res, List<Integer> path, int[] nums, boolean[] flag){
        if(path.size() == nums.length){
            res.add(new ArrayList(path));
            return;
        }
        for(int i = 0; i < nums.length; i++){
            if(!flag[i]){
                flag[i] = true;
                path.add(nums[i]);
                helper(res, path, nums, flag);
                path.remove(path.size()-1);
                flag[i] = false;
            }
        }
    }
    public List<List<Integer>> permute(int[] nums) {
        boolean[] flag = new boolean[nums.length];
        List<List<Integer>> res = new ArrayList<>();
        helper(res, new ArrayList<Integer>(), nums, flag);
        return res;
    }
}

public class Solution {
    
    int[] resetof(int[] num, int index){
        int[] rt = new int[num.length - 1];
        int s = 0;
        for(int i = 0; i < num.length ; i++)
            if(i != index) rt[s++] = num[i];
        
        return rt;
    }
    
    public List<List<Integer>> permute(int[] num) {
        
        ArrayList<List<Integer>> rt = new ArrayList<List<Integer>>();
        
        if(num.length == 0){
            // do nothing
        }else if(num.length == 1) {
            rt.add(new ArrayList<Integer>(Arrays.asList(num[0])));
        }else{
            
            for(int i = 0; i < num.length; i++){
                for(List<Integer> l : permute(resetof(num, i))){
                    l.add(num[i]);
                    rt.add(l);
                };
            }   
            
        }
        
        return rt;

        
    }
}
