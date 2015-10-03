import java.util.*;
public class Solution {
    public int longestConsecutive(int[] nums) {
        Integer[] nums2 = new Integer[nums.length];
        for(int i = 0; i < nums.length; i++) nums2[i] = nums[i];
        HashSet<Integer> set = new HashSet<>(Arrays.asList(nums2));
        Iterator it = set.iterator();
        int res = 0;
        while(it.hasNext()){
            int a = (int)it.next();
            int lens = 1;
            int tmp = a;
            while(set.contains(--tmp)){
                set.remove(tmp);
                lens++;
            }
            tmp = a;
            while(set.contains(++tmp)){
                set.remove(tmp);
                lens++;
            }
            res = Math.max(res, lens);
            set.remove(a);
            it = set.iterator();
        }
        return res;
    }
}
public class Solution {
    public int longestConsecutive(int[] num) {
        
        HashSet<Integer> nums = new HashSet<Integer>();
        
        for(int n : num){
            nums.add(n);
        }
        
        int longest = 0;
        
        for(final int n : num){
            
            int l = 1;

            int nn = n;
            
            nums.remove(n);
            
            while(nums.contains(++nn)){
                l++;
                nums.remove(nn);
            } 
            
            nn = n;
                        
            while(nums.contains(--nn)){
                l++;
                nums.remove(nn);
            } 
            
            longest = Math.max(longest, l);
        }
        
        return longest;
        
    }
}