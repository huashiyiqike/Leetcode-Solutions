public class Solution {
    public int numSquares(int n) {
        if(n == 0){
            return 0;
        }
        int[] count = new int[n+1];
        Arrays.fill(count, Integer.MAX_VALUE);
        count[0] = 0;
		int i = 1;
        while(i*i<=n){
            for(int j = i*i;j < n+1 ; j++){
                count[j]=Math.min(count[j],count[j-i*i]+1);
            }
            i=i+1;
        }
        return count[n];
    }
}