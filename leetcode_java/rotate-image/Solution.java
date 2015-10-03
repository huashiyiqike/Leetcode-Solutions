public class Solution {
    public void rotate(int[][] matrix) {
        for(int i = 0; i < matrix.length/2; i++){
            for(int j = 0; j < matrix[0].length; j++){
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[matrix.length - 1 - i][j];
                matrix[matrix.length - 1 - i][j] = tmp;
            }
        }
        for(int i = 0; i < matrix.length;i++){
            for(int j = i+1; j < matrix[0].length; j++){
                int tmp = matrix[j][i];
                matrix[j][i] = matrix[i][j];
                matrix[i][j] = tmp;
            }
        }
    }
}
// http://www.2cto.com/kf/201410/341031.html
public class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int limit = (n - 1) / 2;
        for (int i = 0; i <= limit; i++) {
            for (int j = i; j < n - 1 - i; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - 1 - j][i];
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
                matrix[j][n - 1 - i] = temp;
            }
        }
    }
}
public class Solution {
    public void rotate(int[][] matrix) {
        
        
        final int mx = matrix.length; 
        final int my = matrix[0].length;
        int x,y;
        
        int t;
        
        int _my = my - 1;
        for(x = 0; x < mx - 1; x++){
            for(y = 0; y < _my; y++){
                int ny = mx - 1 - x;
                int nx = my - 1 - y;
                
                t = matrix[y][x];
                matrix[y][x] = matrix[ny][nx];
                matrix[ny][nx] = t;
                
            }
            _my--;
        }
        
        
        for(x = 0; x < mx ; x++){
            for(y = 0 ; y < my / 2; y++){
                int ny = my - 1 - y;
                int nx = x;
                
                t = matrix[y][x];
                matrix[y][x] = matrix[ny][nx];
                matrix[ny][nx] = t;
            }
        }
        
    }
}