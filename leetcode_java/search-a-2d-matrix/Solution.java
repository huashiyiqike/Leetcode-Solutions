public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int left = 0, right = matrix.length * matrix[0].length-1;
        while(left <= right){
            int mid = (left + right)/2;
            int row = mid / matrix[0].length, col = mid % matrix[0].length;
            if(matrix[row][col] < target) left = mid + 1;
            else if(matrix[row][col] > target) right = mid - 1;
            else return true;
        }
        return false;
    }
}
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        int mx = matrix.length;
        int my = matrix[0].length;
        
        final int count = mx * my;
        
        int l = 0, r = count;
        
        while(l < r){
            int m = (r + l) / 2;
            
            int x = m / my;
            int y = m % my;
            
            if(matrix[x][y] == target)
                return true;
            else if(matrix[x][y] < target)
                l = m + 1;
            else 
                r = m;
                
            
        }
        
        return false;
    }
}