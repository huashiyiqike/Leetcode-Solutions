public class Solution {
    public int minPathSum(int[][] grid) {
        int[][] dp = new int[grid.length][grid[0].length];
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(i == 0 && j == 0) dp[i][j] = grid[i][j];
                else if(i == 0) dp[i][j] = dp[i][j-1] + grid[i][j];
                else if(j == 0) dp[i][j] = dp[i-1][j] + grid[i][j];
                else
                dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        return dp[grid.length-1][grid[0].length-1];
    }
}
public class Solution {
    public int minPathSum(int[][] grid) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        
        
        int mx = grid.length;
        if(mx == 0) return 0;
        
        int my = grid[0].length;
        
        for(int x = 1; x < mx ; x++){
            grid[x][0] += grid[x - 1][0];
        }
        
        for(int y = 1; y < my ; y++){
            grid[0][y] += grid[0][y - 1];
        }
        
        for(int x = 1; x < mx; x++){
            for(int y = 1; y < my; y++){
                grid[x][y] += Math.min(grid[x - 1][y], grid[x][y - 1]);
            }
        }
        
        return grid[mx - 1][my - 1];
    }
}