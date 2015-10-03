class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        tmpdir=x=y=0
        visited={}
        res=[]
        while 0<=x<len(matrix) and 0<=y<len(matrix[0])  and (x,y) not in visited!=None:
            res.append(matrix[x][y])
            visited[(x,y)]=True
            tmpx=x+dir[tmpdir][0]
            tmpy=y+dir[tmpdir][1]
            if tmpx>=len(matrix) or tmpx<0 \
                    or tmpy>=len(matrix[0]) or tmpy<0 \
                    or (tmpx,tmpy) in visited:
                tmpdir+=1
                tmpdir%=len(dir)
            x+=dir[tmpdir][0]
            y+=dir[tmpdir][1]
        return res

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        tmpdir=0
        x=0
        y=0
        res=[]
        while x<len(matrix) and x>=0 and y<len(matrix[0]) and y>=0 and matrix[x][y]!=None:
            res.append(matrix[x][y])
            matrix[x][y]=None
            if x+dir[tmpdir][0]>=len(matrix) or x+dir[tmpdir][0]<0 \
            or y+dir[tmpdir][1]>=len(matrix[0]) or y+dir[tmpdir][1]<0:
                tmpdir+=1
                tmpdir%=len(dir)
            elif matrix[x+dir[tmpdir][0]][y+dir[tmpdir][1]]==None:
                tmpdir+=1
                tmpdir%=len(dir)
                
            x+=dir[tmpdir][0]
            y+=dir[tmpdir][1]
 

        return res
    
if __name__=="__main__":
    a=Solution()
    print a.spiralOrder([[]])
    print a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])