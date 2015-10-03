public class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int count1 = 0, count2 = 0, cur1 = 0, cur2 = 1;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == cur1){
                count1++;
            }else if(nums[i] == cur2){
                count2++;
            }else{
                if(count1 == 0){
                    cur1 = nums[i];
                    count1 = 1;
                }
                else if(count2 == 0){
                    cur2 = nums[i];
                    count2 = 1;
                }else{
                    count1--;
                    count2--;
                }
            }
        }
        count1 = 0;
        count2 = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == cur1) count1++;
            if(nums[i] == cur2) count2++;
        }
        List<Integer> res = new ArrayList<>();
        if(count1 > nums.length/3) res.add(cur1);
        if(count2 > nums.length/3) res.add(cur2);
        return res;
    }
}
public class Solution {
    public List<Integer> majorityElement(int[] nums) {
        if(nums.length == 0) return Collections.emptyList();

        int n1 = nums[0];
        int n2 = nums[0];

        int c1 = 0;
        int c2 = 0;

        for(int i = 0; i < nums.length; i++){

            // put to an empty slot
            if(c1 <= 0 && nums[i] != n2){
                n1 = nums[i];
                c1 = 1;
                continue;
            }

            if(c2 <= 0 && nums[i] != n1){
                n2 = nums[i];
                c2 = 1;
                continue;
            }

            // add count
            if(nums[i] == n1){
                c1++;
                continue;
            }

            if(nums[i] == n2){
                c2++;
                continue;
            }

            // no match

            c1--;
            c2--;
        }

        // faint
        return new ArrayList<>(IntStream.of(n1, n2)
                .filter(n ->
                        Arrays.stream(nums).filter(i -> n == i).count() > nums.length / 3)
                .boxed()
                .collect(Collectors.toSet()));
    }
}
