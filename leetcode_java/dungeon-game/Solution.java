public class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        for(int i = dungeon.length-1; i >= 0; i--){
            for(int j = dungeon[0].length-1; j >=0; j--){
                if(i == dungeon.length-1 && j == dungeon[0].length-1){
                    dungeon[i][j] = Math.max(0, - dungeon[i][j]);
                }
                else if(i == dungeon.length-1){
                    dungeon[i][j] = Math.max(0, dungeon[i][j+1]-dungeon[i][j]);
                }
                else if(j == dungeon[0].length-1){
                    dungeon[i][j] = Math.max(0, dungeon[i+1][j]-dungeon[i][j]);
                }else{
                    dungeon[i][j] =  Math.min(Math.max(0, dungeon[i][j + 1] - dungeon[i][j]),
                            Math.max(0, dungeon[i + 1][j] - dungeon[i][j]));
                }
            }
        }
        return dungeon[0][0]+1;
    }
}

public class Solution {
    
    int minHealthReach(int hp, int room){
        hp -= room;
        if(hp <= 0){
            return 1;
        }

        return hp;
    }
    
    public int calculateMinimumHP(int[][] dungeon) {
        
        final int mx = dungeon.length;
        final int my = dungeon[0].length;
        
        dungeon[mx - 1][my - 1] = minHealthReach(1, dungeon[mx - 1][my - 1]);
        
        for(int i = mx - 2; i >= 0; i--){
            dungeon[i][my - 1] = minHealthReach(dungeon[i + 1][my - 1], dungeon[i][my - 1]);
        }

        for(int j = my - 2; j >= 0; j--){
            dungeon[mx - 1][j] = minHealthReach(dungeon[mx - 1][j + 1], dungeon[mx - 1][j]);
        }


        for(int i = mx - 2; i >= 0; i--){
            for(int j = my - 2; j >= 0; j--){
                dungeon[i][j] = minHealthReach(Math.min(dungeon[i + 1][j], dungeon[i][j + 1]), dungeon[i][j]);
            }
        }
        
        return dungeon[0][0];
        
    }
}
