public class Solution {

    public int singleNumber(int[] A) {
        int[] digits = new int[32];
        for(int i=0;i<32;i++)
        {
            for(int j=0;j<A.length;j++)
            {
                digits[i] += (A[j]>>i)&1;
            }
        }
        int res = 0;
        for(int i=0;i<32;i++)
        {
            res += (digits[i]%2)<<i;
        }
        return res;
    }
}


public class Solution {
    public int singleNumber(int[] A) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if (A.length == 1) return A[0];
        int s = A[0];
        
        for(int i = 1; i< A.length; i++)
            s ^= A[i];
            
        return s;
        
    }
}