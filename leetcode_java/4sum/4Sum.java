public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new  ArrayList<List<Integer>>();
        if(nums == null || nums.length <4){
            return result;
        }
        List<Integer> temp = new ArrayList<Integer>();
        int i , j , k , m;
        int len = nums.length;
        int sum;
        Arrays.sort(nums);
        for(i = 0 ; i < len - 3 ;i++){
           if((i != 0) && (nums[i] == nums[i - 1])){
                continue;
            }
            for(j = i + 1 ; j < len - 2 ;j++){
                if((j != i+1) &&nums[j] == nums[j - 1]){
                    continue;
                }
                k = j + 1;
                m = len - 1;
                while(k < m){
                    sum = nums[i] + nums[j] + nums[k] + nums[m];
                    if(sum == target){
                        temp = new ArrayList<Integer>();
                        temp.add(nums[i]);
                        temp.add(nums[j]);
                        temp.add(nums[k]);
                        temp.add(nums[m]);
                        result.add(temp);
                        k++;
                        m--;
                        while(k < m  && nums[m] == nums[m + 1]){
                        m--;
                        }
                     //System.out.println(m);
                        while(k < m && nums[k] == nums[k - 1]){
                             k++;
                         }
                         
                    }else if(sum < target){
                        k++;
                    }
                    else if(sum > target){
                        m--;
                    }
                    
                }
            
            }
        }
        return result;
    }
}