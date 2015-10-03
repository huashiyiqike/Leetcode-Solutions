public class Solution {
    public void setZeroes(int[][] matrix) {
        int col0 = 1;
        for(int i = 0; i < matrix.length; i++){
            if(matrix[i][0] == 0)
                col0 = 0;
            for(int j = 1; j < matrix[0].length; j++){
                if(matrix[i][j] == 0) {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        for(int i = matrix.length-1; i >= 0; i--){
            for(int j = 1; j < matrix[0].length; j++) {
                if(matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;

            }
            if(col0 == 0) matrix[i][0] = 0;
        }
    }
}
public class Solution {
    public void setZeroes(int[][] matrix) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        if(matrix == null) return;
        int mx = matrix.length;
        if ( mx == 0) return;
        int my = matrix[0].length;
        
        int x, y;
        
        boolean xfz = false, yfz = false;
        
        for(x = 0; x < mx ; x++ ){
            if(matrix[x][0] == 0){
                xfz = true;
                break;
            }
        }
        
        for(y = 0; y < my ; y++ ){
            if(matrix[0][y] == 0){
                yfz = true;
                break;
            }
        }
        
        for(x = 1; x < mx ; x++){
            for(y = 1; y < my ; y++){
                if(matrix[x][y] == 0){
                    matrix[x][0] = 0;
                    matrix[0][y] = 0;
                }
            }
        }
        
        for(x = 1; x < mx ; x++ ){
            if(matrix[x][0] == 0){
                for(y = 0; y < my; y++){
                    matrix[x][y] = 0;
                }
            }
        }
        
        for(y = 1; y < my ; y++ ){
            if(matrix[0][y] == 0){
                for(x = 0; x < mx; x++){
                    matrix[x][y] = 0;
                }
            }
        }
        
        if(xfz){
            for(x = 0; x < mx ; x++ ){
                matrix[x][0] = 0;
            }
        }
        
        if(yfz){
            for(y = 0; y < my ; y++ ){
                matrix[0][y] = 0;
            }
        }        
    }
}