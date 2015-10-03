import java.time.Year;
import java.util.*;

public class Solution {
    public boolean check(int x, int y, int sizex, int sizey, boolean[][] vis){
        return x >= 0 && x < sizex && y >= 0 && y < sizey && !vis[x][y];
    }
    public List<Integer> spiralOrder(int[][] matrix) {
        if(matrix.length == 0) return new LinkedList<>();
        int[][] dir = {{0,1}, {1, 0}, {0, -1}, {-1, 0}};
        int count = 0;
        boolean[][] vis = new boolean[matrix.length][matrix[0].length];

        int x = 0, y = 0;
        List<Integer> res = new LinkedList<>();
        while(check(x,y,matrix.length, matrix[0].length, vis)){
            res.add(matrix[x][y]);
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
        return res;
    }
}
public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int [] dr = new int[]{0,1,0,-1};
        int [] dc = new int[]{1,0,-1,0};

        List<Integer> spiral = new ArrayList<Integer>();
        if(matrix.length ==0) return spiral;

        int R = matrix.length, C = matrix[0].length;
        int dir = 0, newR = 0, newC = 0, count = 0;
        boolean [][] visited = new boolean[R][C];

        while(true) {
            if(count == R*C) break;
            spiral.add(matrix[newR][newC]);
            visited[newR][newC] = true;

            if(newR + dr[dir] < 0
                    || newR + dr[dir] >= R
                    || newC + dc[dir] < 0
                    || newC + dc[dir] >= C
                    || visited[newR + dr[dir]][newC + dc[dir]]
                    ) {
                dir = (dir+1)%4;
            }

            newR = newR + dr[dir];
            newC = newC + dc[dir];

            count += 1;
        }
        return spiral;
    }
}
public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        ArrayList<Integer> rt = new ArrayList<Integer>();
        
        if(matrix.length == 0) return rt;
        
        int x = 0, y = 0, my = matrix.length, mx = matrix[0].length;
        //int dx = 1, dy = 1;
        
        while(x < mx && y < my){
            for(int i = x; i < mx && y < my ; i++){
                rt.add(matrix[y][i]);
            }
            
            y++;
            
            for(int i = y; i< my && x < mx; i++){
                rt.add(matrix[i][mx - 1]);
            }
            
            mx--;
            
            for(int i = mx - 1; i >= x && y < my ; i--){
                rt.add(matrix[my - 1][i]);
            }
            
            my--;
            
            for(int i = my - 1; i >= y && x < mx; i--){
                rt.add(matrix[i][x]);
            }
            
            x++;
                
        }
        
        
        return rt;
        
    }
}
