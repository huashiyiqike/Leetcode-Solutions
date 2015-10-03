class Solution:
    def set0(self, grid, x, y):
        self.vis.add((x, y))
        if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]) or grid[x][y] == '0':
            return
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in dirs:
            if (x+i[0], y+i[1]) not in self.vis:
                self.set0(grid, x+i[0], y+i[1])

        grid[x][y] = '0'

    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        res = 0
        self.vis = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.set0(grid, i, j)
        return res

class Solution:
    def explore(self,grid,x,y):
        res=0
        grid[x][y]='x'
        dir=[[1,0],[-1,0],[0,1],[0,-1]]
        for i in dir:
            tmpx=x+i[0]
            tmpy=y+i[1]
            if tmpx>=0 and tmpx<len(grid) and tmpy>=0 and tmpy<len(grid[0]):
                if grid[tmpx][tmpy]=='1':
                    self.explore(grid,tmpx,tmpy)
        
        
        
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        res=0
        for idx,item in enumerate(grid):
            for idy,x in enumerate(item):
                if x=='1':
                    self.explore(grid,idx,idy)
                    res+=1
                
        return res
    
if __name__=="__main__":
    a=Solution()
    print a.numIslands([['1'],['1']])