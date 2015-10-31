import java.util.*;
public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new LinkedList<>();
        for(int i = 0; i < nums.length; i++){
            if(i > 0 && nums[i] == nums[i-1]) continue;
            int left = i+1, right = nums.length-1;
            while(left<right){
                int tmpsum = nums[left] + nums[right];
                if(tmpsum > -nums[i]) right--;
                else if(tmpsum < -nums[i]) left++;
                else{
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    while(left < nums.length && nums[left] == nums[left-1]) left++;
                }
            }
        }
        return res;
    }
}

public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for(int i = 0; i < nums.length-2; i++){
            if(i > 0 && nums[i] == nums[i-1]) continue;
            int target = - nums[i];
            if(target<0) break;
            Map<Integer, Integer> m = new HashMap<>();
            for(int ii = i+1; ii < nums.length; ii++){

                if(m.get(nums[ii]) != null){
                    res.add(Arrays.asList(nums[i], nums[m.get(nums[ii])], nums[ii]));
                } else{
                    m.put(target - nums[ii], ii);
                    while(ii+1 < nums.length && nums[ii+1] == nums[ii]) ii++;
                }
            }
        }
        return res;
    }
}

public class Solution {
    public List<List<Integer>> threeSum(int[] num) {
        
        Arrays.sort(num);
        
        List<List<Integer>> found = new ArrayList<>();
        
        int pneg = 0 , ppos = num.length - 1;
        
        while(ppos > 0 && num[ppos] >= 0){
            
            while(pneg < ppos && num[pneg] <= 0){
                
                int sum = num[pneg] + num[ppos];

                for(int i  = pneg + 1; i < ppos; i++){
                    if(num[i] + sum == 0){
                        found.add(Arrays.asList(new Integer[]{num[pneg], num[i] ,num[ppos]}));
                        
                        break;
                    }
                }
                
                int old = num[pneg];
                while(pneg < ppos && num[pneg] == old) pneg++;                
            }
            
            pneg = 0;
            
            int old = num[ppos];
            while(ppos > 0 && num[ppos] == old) ppos--;
        }
        
        return found;
    }
}
