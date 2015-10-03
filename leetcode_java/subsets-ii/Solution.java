public class Solution {
    public void helper(int[] nums, int start, List<List<Integer>> res, List<Integer> path){
        res.add(path);
        for(int i = start; i < nums.length; i++){
            if(i != start && nums[i] == nums[i-1]) continue;
            List<Integer> newpath = new ArrayList<>(path);
            newpath.add(nums[i]);
            helper(nums, i+1, res, newpath);
        }
    }
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        helper(nums, 0, res, new ArrayList<>());
        return res;
    }
}
public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] num) {
        Arrays.sort(num);

        return new ArrayList<>(IntStream.range(0, 1 << num.length)
                .mapToObj(mask ->
                                IntStream.range(0, num.length)
                                        .filter(i -> ((1 << i) & mask) > 0)
                                        .map(i -> num[i])
                                        .boxed()
                                        .collect(Collectors.toList())
                )
                .collect(Collectors.toSet()));        
    }
}
