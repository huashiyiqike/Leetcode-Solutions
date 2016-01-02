public class Solution {
    public boolean check(int[][] board, int newrow, int newcol) {
        return 0 <= newrow && newrow <= board.length - 1
                && 0 <= newcol && newcol <= board[0].length - 1;
    }

    public void setNext(int row, int col, int[][] board) {
        int[][] dir = {{0, 1}, {0, -1}, {-1, -1}, {-1, 1}, {-1, 0}, {1, 1}, {1, 0}, {1, -1}};
        int count = 0;
        for (int[] d : dir) {
            int newrow = row + d[0], newcol = col + d[1];
            if (check(board, newrow, newcol)
                    && (board[newrow][newcol] == 1 || board[newrow][newcol] == -1)) {
                count++;
            }
        }
        if(count < 2 || count > 3){
            if(board[row][col] == 1) board[row][col] = -1;
        }
        else if(count == 3 && board[row][col] == 0) board[row][col] = 11;
    }

    public void gameOfLife(int[][] board) {
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                setNext(i, j, board);
            }
        }
        for(int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if(board[i][j] == -1) board[i][j] = 0;
                else if(board[i][j] == 11) board[i][j] = 1;
            }
        }
    }
}