public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        ArrayList<List<Integer>> result = new ArrayList<List<Integer>>();
        if(nums.length<3){
            return result;
        }
        Arrays.sort(nums);
        int len = nums.length;
        int target,start,end;
        for (int i =0 ;i<len ;i++){
            if(i==0||nums[i]>nums[i-1]){
                target =-nums[i];
                start = i+1;
                end =len-1;
                while(start<end){
                    if(nums[start]+nums[end]==target){
                        ArrayList<Integer>temp = new  ArrayList<Integer>();
                        temp.add(nums[i]);
                        temp.add(nums[start]);
                        temp.add(nums[end]);
                        result.add(temp);
                         start++;
                          end--;
                          while(start<end && nums[end]==nums[end+1]){
                              end--;
                          }
                          while(start<end && nums[start]==nums[start-1]){
                              start++;
                          }
                    } else if(nums[start]+nums[end]<target){
                       start++;
                    }else if(nums[start]+nums[end]>target){
                       end--;
                    }
                    
                }
            }
        }
        return result;
    }
}