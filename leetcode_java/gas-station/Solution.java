public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int[] dif = new int[gas.length];
        for(int i = 0; i < gas.length; i++) dif[i] = gas[i] - cost[i];
        int left = 0, start = 0;
        int i = 0;
        for(; i < 2 * gas.length; i++){
            left += dif[i%gas.length];
            if(left < 0){
                left = 0;
                start = i+1;
                if(start > gas.length)
                    return -1;
            }
            else if(i - start + 1 >= gas.length) return start;
        }
        return -1;
    }
}

public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        
        
        int start = 0;
        int from_start = 0;
        
        int total = 0;
        
        for(int i = 0; i < gas.length; i++){
            int left = gas[i] - cost[i];
            total += left;
            from_start += left;
            
            if(from_start < 0){
                from_start = 0;
                start = i + 1; // restart from next station
            }
        }
        
        if(total >= 0){
            return start;
        } 
        
        return -1;
    }
}