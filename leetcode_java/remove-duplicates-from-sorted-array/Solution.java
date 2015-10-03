public class Solution {
    public int removeDuplicates(int[] nums) {
        int cur = 0, i = 0;
        while(i < nums.length){
            while(i+1 < nums.length && nums[i+1] == nums[i]) i++;
            nums[cur++] = nums[i++];
        }
        return cur;
    }
}

public class Solution {
    public int removeDuplicates(int[] A) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        if (A.length == 0) return 0;
        
        int len = 1;
        for(int i = 1; i< A.length; i++){
            if(A[i] != A[i - 1]) {
                for(int j = i - 1 ; j > len - 1 ; j-- )
                    A[j] = A[i];
                
                len++;
            }
        }

        return len;        
    }
}