import java.util.HashMap;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> m = new HashMap<>();
        int[] res = new int[2];
        for(int i = 0; i < nums.length; i++){
            if(m.get(nums[i]) != null){
                res[0] = m.get(nums[i]);
                res[1] = i+1;
                return res;
            }else{
                m.put(target - nums[i], i+1);
            }
        }
        throw new RuntimeException();
    }
}

public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        
        HashMap<Integer, Integer> m = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < numbers.length; i++){
            m.put(target - numbers[i], i);
        }
        
        for(int i = 0; i < numbers.length; i++){
            
            Integer v = m.get(numbers[i]);
            
            if(v != null && v != i){
                return new int[]{i + 1, v + 1};                
            }
        }
        
        throw new RuntimeException();
    }
}
