import java.util.*;
// too slow with list
//public class Solution {
//    static List<Integer> dp = new LinkedList<>(Arrays.asList(new Integer[0]));
//    public int numSquares(int n) {
//        while(dp.size() <= n){
//            int tmp = Integer.MAX_VALUE;
//            for(int i = 1; i * i <= dp.size(); i++){
//                tmp = Math.min(tmp, dp.get(dp.size() - i*i)+1);
//            }
//            dp.add(tmp);
//        }
//        return dp.get(dp.size()-1);
//    }
//}
// static dp
public class Solution {
    static Vector<Integer> dp = new Vector<>(Arrays.asList(0));
    public int numSquares(int n) {
        while(dp.size() <= n){
            int tmp = Integer.MAX_VALUE;
            for(int i = 1; i * i <= dp.size(); i++){
                tmp = Math.min(tmp, dp.get(dp.size() - i*i)+1);
            }
            dp.add(tmp);
        }
        return dp.get(n);
    }
}
public class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        for(int i = 1; i <= n; i++){
            dp[i] = Integer.MAX_VALUE;
            for(int j = 1; j < (int)Math.sqrt(i)+1; j++){
                dp[i] = Math.min(dp[i], dp[i - j*j]+1);
            }
        }
        return dp[n];
    }
}
// still MLE
public class Solution {
    public int numSquares(int n) {
        int step = 0;
        Deque<Integer> queue = new LinkedList<>();
        queue.offer(n);
        Deque<Integer> next = new LinkedList<>();
        while (!queue.isEmpty()) {
            next.clear();
            while (!queue.isEmpty()) {
                int tmp = queue.poll();
                for (int i = (int) Math.sqrt(tmp); i > 0; i--) {
                    if (tmp == i * i) return step + 1;
                    next.offer(tmp - i * i);
                }
            }
            step++;
            queue = new LinkedList<>(next);
        }
        return 0;
    }
}