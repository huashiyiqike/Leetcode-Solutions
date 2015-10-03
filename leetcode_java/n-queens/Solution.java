public class Solution {

    public void helper(int row, int total, List<List<String>> res, List<String> path,
                       boolean[] cols, boolean[] plus, boolean[] minus){
        if(row == total){
            res.add(path);
            return;
        }
        for(int i = 0; i < total; i++){
            if(!cols[i] && !plus[row + i] && !minus[total + row - i]){
                cols[i] = true;
                plus[row + i] = true;
                minus[total + row - i] = true;
                List<String> newpath = new ArrayList<String>(path);
                char[] tmpchar = new char[total];
                for(int ii = 0; ii< tmpchar.length; ii++){
                    if(ii == i) tmpchar[ii] = 'Q';
                    else tmpchar[ii] = '.';
                }
                newpath.add(new String(tmpchar));
                helper(row+1, total, res, newpath, cols, plus, minus);
                cols[i] = false;
                plus[row + i] = false;
                minus[total + row - i] = false;
            }
        }
    }
    public List<List<String>> solveNQueens(int n) {
        boolean[] cols = new boolean[n], plus = new boolean[2*n], minus = new boolean[2*n];
        List<List<String>> res = new ArrayList<>();
        helper(0, n, res, new ArrayList<String>(), cols, plus, minus);
        return res;
    }
}
public class Solution {
    boolean[][] chessboard;
    
    int target;
    
    ArrayList<String[]> rt;
    
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
            
            String[] valid = new String[target + 1];
            
            for(int i = 0; i <= target ; i++){
                char[] s = new char[target + 1];
                for(int j = 0; j <= target; j++){
                    s[j] = chessboard[i][j] ? 'Q' : '.';
                }
                
                valid[i] = new String(s);
            }
            
            rt.add(valid);
            
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
    
    public List<String[]> solveNQueens(int n) {
        chessboard = new boolean[n][n];
        target = n - 1;
        
        rt = new ArrayList<String[]>();
        
        search(0);
        
        return rt;
    }
}
