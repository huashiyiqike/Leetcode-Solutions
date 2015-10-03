import java.util.*;


public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        Integer[] idxsort = new Integer[nums.length];
        for(int i = 0; i < nums.length; i++){
            idxsort[i] = i;
        }
        Arrays.sort(idxsort, new Comparator<Integer>(){
            @Override
            public int compare(Integer a, Integer b){
                if(nums[a] < nums[b]) return -1;
                else if(nums[a] > nums[b]) return 1;
                return 0;
            }
        });
        for(int i = 0; i < nums.length; i++){
            int j = i+1;
            while(j < nums.length && (long)nums[idxsort[j]] - (long)nums[idxsort[i]] <= t){
                if( Math.abs(idxsort[i] - idxsort[j]) <= k) return true;
                j += 1;
            }

        }
        return false;
    }
}

public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        Long tt = new Long(t);
        TreeSet<Long> window = new TreeSet<>();
        for(int i = 0; i < nums.length; i++){
            if(window.floor(nums[i] + tt) != null && window.floor(nums[i] + tt) >= nums[i] - t )
                return true;
            window.add(new Long(nums[i]));
            if(i >= k)
                window.remove(new Long(nums[i-k]));
        }
        return false;
    }
}
public class Solution {
    public boolean containsNearbyAlmostDuplicate(final int[] nums, int kk, long t) {
        if (nums.length < 2) return false;
        if (kk == 0) return false;
        TreeSet<Long> window = new TreeSet<>();

        for(int i=0;i<nums.length;i++) {
            // check dup, window size <= kk right now
            if ( window.floor(nums[i] + t) !=null && window.floor(nums[i]+t) >= nums[i]-t )
                return true;
            window.add(new Long(nums[i]));
            if (i >= kk) {
                //remove one, the size has to be kk on the next fresh step
                window.remove(new Long(nums[i-kk]));
            }
        }
        return false;
    }
}
public class Solution {
    
    static class Tree {
        TreeMap<Integer, Integer> tree = new TreeMap<>();

        int size = 0;

        void add(Integer n){
            Integer v = tree.get(n);

            if(v == null){
                v = 0;
            }

            tree.put(n, v + 1);

            size++;
        }

        void remove(Integer n){
            Integer v = tree.get(n);

            v--;

            if(v == 0){
                tree.remove(n);
            } else {
                tree.put(n, v);
            }

            size--;
        }

        // fuck overflow
        long nearSub(Integer n){

            Integer v = tree.get(n);
            if(v >= 2) return 0;

            long min = Long.MAX_VALUE;

            Integer h = tree.higherKey(n);
            if(h != null){
                min = h - n;
            }

            Integer l = tree.lowerKey(n);
            if(l != null){
                min = Math.min(min, (long)n - l);
            }

            return min;
        }
    }

    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (k <= 0) return false;
        if (nums.length <= 1) return false;

        Tree tree = new Tree();

        tree.add(nums[0]);

        int p = 0;
        for(int i = 1; i < nums.length; i++){

            tree.add(nums[i]);

            if(tree.nearSub(nums[i]) <= t){
                return true;
            }

            if(tree.size > k){
                tree.remove(nums[p++]);
            }
        }

        return false;
    }
}
