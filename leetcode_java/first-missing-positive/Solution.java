public class Solution {
    public int firstMissingPositive(int[] nums) {
        int idx = 0;
        while(idx < nums.length){
            while(nums[idx] > 0 && nums[idx] <= nums.length
                    && nums[idx] != nums[nums[idx]-1]){
                int tmp = nums[nums[idx]-1];
                nums[nums[idx]-1] = nums[idx];
                nums[idx] = tmp;
            }
            idx++;
        }
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != i+1) return i+1;
        }
        return nums.length+1;
    }
}
public class Solution {
    public int firstMissingPositive(int[] A) {
        
        final int N = A.length;
        
        next:
        for(int i = 0; i < N; i++){
            int v = A[i];
            
            if(v == i + 1) continue ;

            while(true){
                if(v <= 0 || v > N){
                    continue next;
                }
                
                int t = A[v - 1];
                
                if(t == v){
                    continue next;
                }
                
                A[v - 1] = v;
                v = t;
            }
            
        }
        
        for(int i = 0; i < N; i++){
            int v = A[i];
            
            if (v != i + 1){
                return i + 1;
            }
        }
        
        return N + 1;
        
    }
}