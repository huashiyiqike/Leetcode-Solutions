import java.util.*;
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int[][] dp = new int[2][triangle.size()];
        for(int i = 0; i < 2; i++) Arrays.fill(dp[i], 0);
        dp[0][0] = triangle.get(0).get(0);
        int count = 0;
        for(int i = 1; i < triangle.size(); i++){
            count = (count+1)%2;
            List<Integer> tmplist = triangle.get(i);
            dp[count%2][0] = tmplist.get(0) + dp[(count+1)%2][0];
            int len = tmplist.size();
            for(int j = 1; j < len-1; j++){
                dp[count%2][j] = Math.min(dp[(count+1)%2][j],
                        dp[(count+1)%2][j-1]) + tmplist.get(j);
            }
            dp[count%2][len-1] = tmplist.get(len-1) +
                    dp[(count+1)%2][len-2];
        }
        int res = Integer.MAX_VALUE;
        for(int i = 0; i < dp[0].length; i++){
            res = Math.min(res, dp[count][i]);
        }
        return res;
    }
}
public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {

        final int size = triangle.size();
        if(size == 0) return 0;
        if(size == 1) return triangle.get(0).get(0);
        
        int[] s = new int[size];
        
        int i = 0;
        for(int v : triangle.get(size - 1)){
             s[i++] = v;
        }
        
        for(i = size - 2; i >=0 ; i--){
            List<Integer> step = triangle.get(i);
            
            // s[0] = min(s[0] + step[0], s[1] + step[0])
            
            for(int j = 0; j < step.size(); j++){
                s[j] = Math.min(step.get(j) + s[j], step.get(j) + s[j + 1]);
            }
            
        }

        return s[0];
    }
}
