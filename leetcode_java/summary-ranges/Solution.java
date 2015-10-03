public class Solution {
    public List<String> summaryRanges(int[] nums) {
        int idx = 0;
        List<String> res = new ArrayList<>();
        while(idx < nums.length){
            int end = idx;
            while(end+1 < nums.length && nums[end+1]==nums[end]+1) end++;
            if(end == idx) res.add(nums[idx]+"");
            else  res.add(nums[idx]+"->"+nums[end]);
            idx = end + 1;
        }
        return res;
    }
}

public class Solution {

    static class Range {

        int st;
        int ed;

        Range(int st){
            this.st = st;
            this.ed = st;
        }

        public String toString(){
            if(ed == st) return "" + st;

            return st + "->" + ed;
        }
    }

    public List<String> summaryRanges(int[] nums) {

        ArrayList<String> rt = new ArrayList<>();

        if(nums.length == 0) return rt;

        Range r = new Range(nums[0]);

        for(int i = 1; i < nums.length; i++){
            if(nums[i] - r.ed == 1){
                r.ed = nums[i];
            } else {
                rt.add(r.toString());
                r = new Range(nums[i]);
            }
        }

        rt.add(r.toString());

        return rt;
    }
}
