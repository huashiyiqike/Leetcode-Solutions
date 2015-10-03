public class Solution {
    public int factorial(int n){
        if(n == 1 || n == 0) return 1;
        return factorial(n-1)*n;
    }
    public String getPermutation(int n, int k) {
        List<Integer> nums = new ArrayList<>();
        String res = "";
        for(int i = 0; i < n; i++) nums.add(i+1);
        k--;
        for(int i = 0; i < n; i++){
            int tmp = factorial(n-1-i);
            int index = k/tmp;
            k %= tmp;
            res += String.valueOf(nums.get(index));
            nums.remove(index);
        }
        return res;
    }
}

public class Solution {
    
    int fact(int x){
        int s = 1;
        
        for(int i = 1; i <= x; i++)
            s *= i;
            
        return s;
    }

    public String getPermutation(int n, int k) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        ArrayList<Character> chars = new ArrayList<Character>();
        
        for(int i = '1'; i <('1' + n); i++) 
            chars.add((char)i);
        
        k -= 1;
        
        char[] t = new char[n];
        int l = 0;
         
        for(int i = n - 1; i > 0; i--){
            int f = fact(i);
            
            int c = k / f;
              
            t[l++] = chars.get(c);
            chars.remove(c);
            
            k %= f;
        }
        
        t[n - 1] = chars.get(0);

        return new String(t);
        
    }
}