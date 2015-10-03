public class Solution {
    public int maxProfit(int[] prices) {
        int res = 0, mins = Integer.MAX_VALUE;
        for(int i = 0; i < prices.length; i++){
            mins = Math.min(mins, prices[i]);
            res = Math.max(res, prices[i] - mins);
        }
        return res;
    }
}
public class Solution {
    public int maxProfit(int[] prices) {
        
        int max = 0;
        
        int lowest = Integer.MAX_VALUE;
        
        for(int p : prices){
    
            lowest = Math.min(lowest, p);
            
            max = Math.max(p - lowest, max);
        }
        
        return max;
    }
}
