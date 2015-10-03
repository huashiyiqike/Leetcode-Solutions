public class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                dp[i][j] = 1;
        for(int i = 1; i < m; i++){
            for(int j = 0; j < n; j++){
                if(j > 0) dp[i][j] = dp[i-1][j] + dp[i][j-1];
                else dp[i][j] = dp[i-1][j];
            }
        }
        return dp[m-1][n-1];
    }
}
public class Solution {
    public int uniquePaths(int m, int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        if(m == 0 || n == 0) return 0;
        
        int[][] matrix = new int[m][n];
        
        int x, y;
        
        for(x = 0; x < m; x++)
            matrix[x][0] = 1;
        
        for(y = 0; y < n; y++)
            matrix[0][y] = 1;
            
        
        for(x = 1; x < m; x++){
            for(y = 1; y < n; y++){
                matrix[x][y] = matrix[x - 1][y] + matrix[x][y - 1];
            }
        }
        
        return matrix[m - 1][n - 1];
    }
}