import java.util.LinkedList;
import java.util.List;

public class Solution {
    public boolean check(int x, int y, int sizex, int sizey, boolean[][] vis){
        return x >= 0 && x < sizex && y >= 0 && y < sizey && !vis[x][y];
    }
    public int[][] generateMatrix(int n) {
        if(n == 0) return new int[][]{};
        int[][] matrix = new int[n][n];
        int[][] dir = {{0,1}, {1, 0}, {0, -1}, {-1, 0}};
        int count = 0;
        boolean[][] vis = new boolean[matrix.length][matrix[0].length];

        int x = 0, y = 0;
        for(int num = 1; num <= n*n; num++){
            matrix[x][y] = num;
            vis[x][y] = true;
            int tmpx = x + dir[count][0];
            int tmpy = y + dir[count][1];
            if(tmpx < 0 || tmpx >= matrix.length || tmpy < 0 || tmpy >= matrix[0].length ||
                    vis[x + dir[count][0]][y + dir[count][1]]){
                count = (count+1)%4;
            }
            x += dir[count][0];
            y += dir[count][1];
        }
        return matrix;
    }
}
public class Solution {
    public int[][] generateMatrix(int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        int[][] rt = new int[n][n];
        if(n <= 0) return rt;
        
        int c = 1;
        
        int x = 0, y = 0, my = n , mx = n;
        
        while(x < mx && y < my){
            for(int i = x; i < mx && y < my; i++){
                rt[y][i] = c++;
            }
            
            y++;
            
            for(int i = y; i < my && x < mx ; i++ ){
                rt[i][mx - 1] = c++;
            }
            
            mx--;
            
            for(int i = mx - 1; i >= x && y < my; i--){
                rt[my - 1][i] = c++;
            }
            
            my--;
            
            for(int i = my - 1; i>= y && x < mx; i--){
                rt[i][x] = c++;
            }
            
            x++;
            
        }
        
        return rt;
        
        
    }
}