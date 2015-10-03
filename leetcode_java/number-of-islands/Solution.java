import java.util.Set;

public class Solution {
    public boolean check(int x, int y, int rows, int cols){
        return x >= 0 && x < rows && y >= 0 && y < cols;
    }
    public void helper(char[][] grid, boolean[][] visited, int x, int y){
        visited[x][y] = true;
        grid[x][y] = '0';
        int[][] dir = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        for(int i = 0; i < dir.length; i++){
            if(check(x + dir[i][0], y + dir[i][1], grid.length, grid[0].length)
                    && grid[x + dir[i][0]][y + dir[i][1]] == '1')
                    helper(grid, visited, x + dir[i][0], y + dir[i][1]);
        }
    }
    public int numIslands(char[][] grid) {
        if(grid.length == 0) return 0;
        int res = 0;
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){

                if(grid[i][j] == '1') {
                    res++;helper(grid, visited, i, j);
                }
            }
        }
        return res;
    }
}
public class Solution {

    boolean allowed(int x, int y, final int mx, final int my, char[][] grid, boolean[][] visited){
        return (x < mx) && (x >= 0)
            && (y < my) && (y >= 0)
            && (grid[x][y] == '1')
            && (!visited[x][y]);
    }

    void travel(int x, int y, final int mx, final int my, char[][] grid, boolean[][] visited){

        // x - 1, y
        // x + 1, y
        // x, y - 1
        // x, y + 1

        visited[x][y] = true;

        for(int[] xy: new int[][]{ {x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1} }){

            int _x = xy[0];
            int _y = xy[1];

            if(allowed(_x, _y, mx, my, grid, visited)){
                travel(_x, _y, mx, my, grid, visited);
            }
        }

    }

    public int numIslands(char[][] grid) {

        final int mx = grid.length;
        if(mx == 0) return 0;
        final int my = grid[0].length;

        int count = 0;
        boolean[][] visited = new boolean[mx][my];

        for(int x = 0; x < mx; x++){
            for(int y = 0; y < my; y++){
                if(allowed(x, y, mx, my, grid, visited)){

                    travel(x, y, mx, my, grid, visited);

                    count++;
                }
            }
        }

        return count;
    }
}
