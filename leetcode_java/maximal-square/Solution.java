public class Solution {
    public int maximalSquare(char[][] matrix) {
        if(matrix.length == 0) return 0;
        int[][] dp = new int[matrix.length][matrix[0].length];
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                dp[i][j] = (matrix[i][j] == '0'?0:1);
            }
        }
        for(int i = 1; i < matrix.length; i++){
            for(int j = 1; j < matrix[0].length; j++){
                if(matrix[i][j] == '0') dp[i][j] = 0;
                else{
                    dp[i][j] = Math.min(dp[i-1][j], Math.min(dp[i][j-1], dp[i-1][j-1]))+1;
                }
            }
        }
        int res = 0;
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                res = Math.max(res, dp[i][j]);
            }
        }
        return res*res;
    }
}
public class Solution {
    
    int maximalSquare(char[][] matrix, final int x, final int y){
        int l = 1;
        
        done:
        while(true){
        
            for(int i = 0; i <= l; i++){
                
                if(x + l >= matrix.length || y + l >= matrix[0].length){
                    break done;
                }
                
                
                if(matrix[x + l][y + i] != '1'){
                    break done;
                }
                
                if(matrix[x + i][y + l] != '1'){
                    break done;
                }
                
            }
            
            l++;
        }
        
        return l * l;
    }
    
    public int maximalSquare(char[][] matrix) {
        
        int max = 0;
        
        for(int x = 0; x < matrix.length; x++){
            for(int y = 0; y < matrix[0].length; y++){
                if(matrix[x][y] == '1'){
                    max = Math.max(max, maximalSquare(matrix, x, y));
                }
            }
        }
        
        return max;
    }
}
