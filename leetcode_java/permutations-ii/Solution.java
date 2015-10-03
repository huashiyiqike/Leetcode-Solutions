public class Solution {
    public void helper(List<List<Integer>> res, int[] nums, List<Integer> path, boolean[] flag){
        if(path.size() == nums.length){
            res.add(new ArrayList(path));
            return;
        }
        for(int i = 0; i < nums.length; i++){
            if(!flag[i] &&( i == 0 || !(flag[i-1] && nums[i] == nums[i-1])  )){
                flag[i] = true;
                path.add(nums[i]);
                helper(res, nums, path, flag);
                path.remove(path.size()-1);
                flag[i] = false;
            }
        }
    }
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        boolean[] flag = new boolean[nums.length];
        helper(res, nums, new ArrayList<>(), flag);
        return res;
    }
}
public class Solution {
    
    void swap(int x[], int a, int b) {
    	int t = x[a];
    	x[a] = x[b];
    	x[b] = t;
    }
    
    public boolean nextPermutation(int[] num) {
        
        if(num.length < 2) return false;
    
        int p = -1;
        
        for(int i = num.length - 1; i >0; i--){
            if(num[i] > num[i - 1]){
                 p = i - 1;
                 break;
            }
        }
        
        if(p == -1){
            Arrays.sort(num);
            return false;
        }
        
        int c = -1;
        for(int i = num.length - 1; i >=0; i--){
            if(num[i] > num[p]) {
                c = i;
                break;
            }
        }
        
        swap(num, p, c);
        Arrays.sort(num, p + 1, num.length);
        
        return true;
    }    
    
    List<Integer> asList(int[] num){
        ArrayList<Integer> l = new ArrayList<Integer>(num.length);
        for(int i = 0; i < num.length; i++)
            l.add(num[i]);
        
        return l;
    }
    
    public List<List<Integer>> permuteUnique(int[] num) {
        Arrays.sort(num);
        
        ArrayList<List<Integer>> found = new ArrayList<List<Integer>>();
        found.add(asList(num));
        
        while(nextPermutation(num)){
            found.add(asList(num));
        }
        
        return found;
    }
}
