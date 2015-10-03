import java.util.ArrayList;
import java.util.HashSet;

public class Solution {
    char[][] board_;
    char[] word_;
    boolean[][] visited;
    public boolean helper(int x, int y, int word_idx){
        if(x < 0 || x >= board_.length || y < 0 || y >= board_[0].length ||
                board_[x][y] != word_[word_idx] || visited[x][y]) return false;
        if(word_idx == word_.length - 1) return true;

        visited[x][y] = true;
        word_idx++;
        boolean res = helper(x+1, y, word_idx) || helper(x-1, y, word_idx)||
                helper(x, y+1, word_idx) || helper(x, y-1, word_idx);

        // the same
//        boolean res = false;
//        int[][] dir = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
//        for(int[] i : dir){
//            if(helper(x + i[0], y + i[1], word_idx + 1)) {
//                res = true;
//                break;
//            }
//        }

        visited[x][y] = false;
        return res;
    }
    public boolean exist(char[][] board, String word) {
        board_ = board;
        word_ = word.toCharArray();
        visited = new boolean[board.length][board[0].length];
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(helper(i, j, 0)) return true;
            }
        }
        return false;
    }
}

public class Solution {
    
    class XY{
        int x;
        int y;
        
        XY(int x, int y) { 
            this.x = x; 
            this.y = y;
        }
    }
    
    XY[] stack;
    
    int mx;
    int my;
    
    boolean search(char[][] board, char[] cs, final int index){
        
        if(index >= cs.length) return true;
        
        // final int mx = board.length, my = board[0].length;

        final int x = stack[index - 1].x, y = stack[index - 1].y;
        
        next:
        for(XY xy : new XY[]{new XY(x - 1, y), new XY(x + 1, y), new XY(x, y - 1), new XY(x, y + 1) }){
            int _x = xy.x;
            int _y = xy.y;
            
            for(int i = 0; i < index ; i++){
                if(stack[i].x == _x && stack[i].y == _y)
                    continue next;
            }
            
            if(_x >=0 && _x < mx && _y >= 0 && _y < my){
                if(board[_x][_y] == cs[index]){
                    stack[index] = new XY(_x , _y);
                    
                    if(search(board, cs, index + 1))
                        return true;
                }
            }
            
        }
        
        return false;
    }
    
    
    public boolean exist(char[][] board, String word) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        
        if (board.length == 0) return false;
        
        
        int x = 0, y = 0;

        mx = board.length;
        my = board[0].length;
        
        char[] str = word.toCharArray();
        
        
        //if( str.length > mx * my ) return false; // fuck..
        
        stack = new XY[str.length];
        
        if(str.length == 0) return false;
        
        for(x = 0; x < mx; x++){
            for(y = 0; y < my; y++){
                if( board[x][y] == str[0] ){
                    
                    stack[0] = new XY(x, y);
                    if(search(board, str, 1))
                        return true;
                }
            }
        }
        
        return false;
    }
}