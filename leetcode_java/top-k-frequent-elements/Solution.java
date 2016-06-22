public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        List<Integer> result = new ArrayList<Integer>();
        if(nums ==  null || nums.length == 0 || k<= 0){
            return result;
        }
        int len = nums.length;
        HashMap<Integer,Integer> map =  new HashMap<Integer,Integer>();
        for(int i = 0 ;i < len ;i++){
            if(map.containsKey(nums[i])){
                map.put(nums[i],map.get(nums[i])+1);
            }else{
                map.put(nums[i],1);
            }
        }
        List<Integer>[] arr = new ArrayList[len+1];
        for(Integer i : map.keySet()){
            int fre = map.get(i);
            if(arr[fre] == null){
                arr[fre] = new ArrayList();
            }
            arr[fre].add(i);
        }
        int size;
        for(int i = len;i > 0 && k > 0 ; i--){
            if(arr[i] != null){
                size = arr[i].size();
                for(int j = 0; j < size && k > 0; j++){
                    result.add(arr[i].get(j));
                    k--;
                }
            }
         }
        return result;
    }
}