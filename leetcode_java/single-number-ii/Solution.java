public class Solution {
    public int singleNumber(int[] nums) {
        int[] bits = new int[32];
        for(int i = 0; i < 32; i++){
            for(int n:nums){
                if((n>>>i & 1) == 1) bits[i]++; // >> is also right
            }
        }
        int res = 0;
        for(int i = 0; i < 32; i++){
            if(bits[i]%3 == 1) res |= 1<<i;
        }
        return res;
    }
}

public class Solution {
    public int singleNumber(int[] A) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        int[] count = new int[Integer.SIZE];
        int[] bit   = new int[Integer.SIZE];
        
        Arrays.fill(count, 0);
        Arrays.fill(bit, 0);
        
        for(int a : A){
            
            for(int b = 0; b < Integer.SIZE; b++){
                int x = a >>> b & 1;
                bit[b] |= x;

                if(x == 1)
                    count[b]++;
            }
            
        }
        
        int s = 0;
        for(int b = 0; b < Integer.SIZE; b++ ){
            if (count[b] % 3 != 0)
                s |= bit[b] << b;
        }
        
        return s;
        
    }
}