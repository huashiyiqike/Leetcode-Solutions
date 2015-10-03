import java.util.*;
public class Solution {
    public void helper(int[] nums, int start, List<List<Integer>> res, List<Integer> path){
        res.add(path);
        for(int i = start; i < nums.length; i++){
            List<Integer> newpath = new ArrayList<>(path);
            newpath.add(nums[i]);
            helper(nums, i+1, res, newpath);
        }
    }
    public List<List<Integer>> subsets(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        helper(nums, 0, res, new ArrayList<>());
        return res;
    }
}
public class Solution {
    public List<List<Integer>> subsets(int[] S) {
        Arrays.sort(S);

        return IntStream.range(0, 1 << S.length)
                .mapToObj(mask -> 
                    IntStream.range(0, S.length)
                        .filter(i -> ((1 << i) & mask) > 0)
                        .map(i -> S[i])
                        .boxed()
                        .collect(Collectors.toList())
                )
                .collect(Collectors.toList());        
    }
}
