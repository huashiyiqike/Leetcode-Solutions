import java.util.*;
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int res = Integer.MAX_VALUE, fina = 0;
        for(int i = 0; i< nums.length-2;i++) {
            int aim = target - nums[i];
            int left = i + 1, right = nums.length-1;
            while (left < right) {
                int tmpsum = nums[left] + nums[right];
                if(Math.abs(tmpsum - aim) < res) {
                    res = Math.min(Math.abs(tmpsum - aim), res);
                    fina = tmpsum + nums[i];
                }
                if (tmpsum > aim) right--;
                else left++;
            }
        }
        return fina;
    }
}

public class Solution {
    public int threeSumClosest(int[] num, int target) {
        
        if(num.length < 3) return 0;
        
        Arrays.sort(num);
        
        int pneg = 0 , ppos = num.length - 1;
        
        int closest = num[0] + num[1] + num[2];
        
        while(ppos > 0){
            while(pneg < ppos){
                int sum = num[pneg];
                sum += num[ppos];
                
                for(int i  = pneg + 1; i < ppos; i++){
                    if(Math.abs(target - (num[i] + sum)) < Math.abs(target - closest) ){
                        closest = num[i] + sum;
                    }
                }
                
                int old = num[pneg];
                while(pneg < ppos && num[pneg] == old) pneg++;                
            }
            
            pneg = 0;
            
            int old = num[ppos];
            while(ppos > 0 && num[ppos] == old) ppos--;
        }
        
        
        return closest;
    }
}