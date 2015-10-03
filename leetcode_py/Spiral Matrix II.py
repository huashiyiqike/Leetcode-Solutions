class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        res=[[False for i in range(n)] for j in range(n)]
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        x=0
        y=0
        d=0
        for i in range(1,n*n+1):
          #  print i,x,y
            res[x][y]=i
            if x+dir[d][0]<0 or x+dir[d][0]>n-1 or y+dir[d][1]<0 or y+dir[d][1]>n-1\
            or res[x+dir[d][0]][y+dir[d][1]]!=False:
                d=(d+1)%4 
            x+=dir[d][0]
            y+=dir[d][1]
            
        return res
    
if __name__=="__main__":
    a=Solution()
    print a.generateMatrix(3)
    print a.generateMatrix(4)   