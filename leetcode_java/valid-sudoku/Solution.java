public class Solution {
    public boolean isValidSudoku(char[][] board) {
        // board is 9*9
        boolean[][] rows = new boolean[9][9], cols = new boolean[9][9];
        boolean[][][] x = new boolean[3][3][9];
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] != '.'){
                    int idx = (int)board[i][j] - (int)'1';//Integer.parseInt(board[i][j]+"");
                    if(cols[j][idx] || rows[i][idx] || x[i/3][j/3][idx]) return false;
                    rows[i][idx] = true;
                    cols[j][idx] = true;
                    x[i/3][j/3][idx] = true;

                }
            }
        }
        return true;
    }
}

public class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        int mx = board.length;
        int my = board[0].length;
        
        int x, y;
        
        for(x = 0; x < mx; x++){
            HashSet<Character> col = new HashSet<Character>();
            for(y = 0; y < my; y++){
                char c = board[x][y];
                if(c != '.'){
                    if(col.contains(c)) return false;
                    
                    col.add(c);
                } 
            }
        }
        
        for(y = 0; y < my; y++){
            HashSet<Character> row = new HashSet<Character>();
            for(x = 0; x < mx; x++){
                char c = board[x][y];
                if(c != '.'){
                    if(row.contains(c)) return false;
                    
                    row.add(c);
                } 
            }
        }
        
        for(x = 0; x < mx; x += 3){
            for(y = 0; y < my; y += 3){
                
                HashSet<Character> block = new HashSet<Character>();
                
                for(int offset = 0; offset < 9; offset++){
                    int ox = offset % 3;
                    int oy = offset / 3;
                    
                    char c = board[x + ox][y + oy];
                    if(c != '.'){
                        if(block.contains(c)) return false;
                    
                        block.add(c);
                    } 
                }
            }
        }
        
        return true;
    }
}