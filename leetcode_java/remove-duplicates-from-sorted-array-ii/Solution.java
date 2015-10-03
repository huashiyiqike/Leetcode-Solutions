public class Solution {
    public int removeDuplicates(int[] nums) {
        int cur = 0, i = 0;
        while(i < nums.length){
            nums[cur++] = nums[i];
            if(i+1 < nums.length && nums[i+1] == nums[i]) {
                while (i + 1 < nums.length && nums[i + 1] == nums[i]) i++;
            }else {
                i++;
            }
        }
        return cur;
    }
}

public class Solution {
    public int removeDuplicates(int[] A) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        if(A.length == 0) return 0;
        
        int len = 1;
        int lastseencount = 0;

        for(int i = 1; i< A.length; i++){
            if(A[i] != A[i - 1]){
                
                for(int j = i - 1; j > len + Math.min(lastseencount, 1) - 1 ; j--)
                    A[j] = A[i];
                
                len += Math.min(lastseencount, 1) + 1;
                lastseencount = 0;
            }else{
                lastseencount++;
            }
        }
        
        return len + Math.min(lastseencount, 1);
    }
}