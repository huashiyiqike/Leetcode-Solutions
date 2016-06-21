public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer>map = new HashMap<Integer,Integer>();
       int len=nums.length;
        int[] index=new int[2];
        int temp;
        for(int i =0 ;i<len;i++){
            if(map.containsKey(target-nums[i])){
                index[0] =i+1;
                index[1]=map.get(target-nums[i])+1;
                if(index[0]>index[1]){
                    temp =index[0];
                    index[0]=index[1];
                    index[1]=temp;
                }
                break;
            }else{
            map.put(nums[i],i);
                
            }
        }
        
        return index;
    }
}