public class Solution {
    public int totalNQueens(int n) {
        boolean[] cols = new boolean[n], plus = new boolean[2*n], minus = new boolean[2*n];
        int[] res = new int[1];
        res[0] = 0;
        helper(0, n, res, cols, plus, minus);
        return res[0];
    }

    public void helper(int row, int total, int[] res,
                       boolean[] cols, boolean[] plus, boolean[] minus){
        if(row == total){
            res[0]++;
            return;
        }
        for(int i = 0; i < total; i++){
            if(!cols[i] && !plus[row + i] && !minus[total + row - i]){
                cols[i] = true;
                plus[row + i] = true;
                minus[total + row - i] = true;
                helper(row+1, total, res, cols, plus, minus);
                cols[i] = false;
                plus[row + i] = false;
                minus[total + row - i] = false;
            }
        }
    }
}
public class Solution {
    
    boolean[][] chessboard;
    
    int target;
    
    int rt;
    
    boolean tryput(final int row, final int col){
        for(int i = row - 1; i >= 0; i--){
            int offset = row - i;
            if(chessboard[i][col])
                return false;
            
            if(col - offset >= 0 && chessboard[i][col - offset])
                return false;
                
            if(col + offset <= target && chessboard[i][col + offset])
                return false;
        }
        
        return true;
    }
    
    void search(final int row){
        
        if( row > target){
            
            rt++;
            
            return;
        }
        
        for(int i = 0; i <= target ; i++){
            if(tryput(row, i)){
                
                chessboard[row][i] = true;    
            
                search(row + 1);
                
                chessboard[row][i] = false;  
            }
        }
        
    }
    
    public int totalNQueens(int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        chessboard = new boolean[n][n];
        target = n - 1;
        
        rt = 0;
        
        search(0);
        
        return rt;
    }
}