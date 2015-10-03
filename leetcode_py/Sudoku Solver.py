class Solution:
    def helper(self, board, idx, idy):
        if idy > 8:
            return self.helper(board, idx+1, 0)
        if idx > 8:
            return True
        if board[idx][idy] != '.':
            return self.helper(board, idx, idy+1)
        for i in range(9):
            if self.row[idx][i] or self.col[idy][i] or self.x[idx/3][idy/3][i]:
                continue
            self.row[idx][i] = True
            self.col[idy][i] = True
            self.x[idx/3][idy/3][i] = True
            if self.helper(board, idx, idy+1):
                board[idx][idy] = str(i+1)
                return True
            self.row[idx][i] = False
            self.col[idy][i] = False
            self.x[idx/3][idy/3][i] = False
        return False


    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        self.row = [[False] * 9 for _ in range(9)]
        self.col = [[False] * 9 for _ in range(9)]
        self.x  = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        for idx, item in enumerate(board):
            for idy, char in enumerate(item):
                if char != '.':
                    self.row[idx][int(char)-1] = True
                    self.col[idy][int(char)-1] = True
                    self.x[idx/3][idy/3][int(char)-1] = True
        self.helper(board, 0, 0)


class Solution:
    def f(self, board, x, y, rows, cols, small):
        if board[x][y] != '.':
            if y < len(board[0])-1:
                return self.f(board, x, y+1, rows, cols, small)
            elif x < len(board)-1:
                return self.f(board, x+1, 0, rows, cols, small)
            elif x == len(board)-1 and y == len(board[0])-1:
                return True
        nextx = x
        nexty = y
        if y < len(board[0]) - 1:
            nexty += 1
        elif x < len(board)-1:
            nextx += 1
            nexty = 0

        for i in range(9):
            if rows[x][i] or cols[y][i] or small[(x/3)*3 + y/3][i]:
                continue
            board[x][y] = str(i+1)
            rows[x][i] = True
            cols[y][i] = True
            small[(x/3)*3 + y/3][i] = True
            if self.f(board, nextx, nexty, rows, cols, small):
                return True
            board[x][y] = '.'
            rows[x][i] = False
            cols[y][i] = False
            small[(x/3)*3 + y/3][i] = False
        return False

    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        myboard = [['.']*len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    myboard[i][j] = board[i][j]

        rows = [[False]*10 for i in range(9)]
        cols = [[False]*10 for i in range(9)]
        small = [[False]*10 for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    rows[i][int(myboard[i][j])-1] = True
                    cols[j][int(myboard[i][j])-1] = True
                    small[(i/3)*3+j/3][int(myboard[i][j])-1] = True
        self.f(myboard, 0, 0, rows, cols, small)
        for i in range(len(board)):
            board[i] = ''.join(myboard[i])
        return board

class Solution:
    def dfs(self,startx,starty):
        if startx==9:
            return True

        i=startx
        j=starty

        if self.board[i][j]=='.':
            for m in range(9):
                if not self.row[i][m] and not self.col[j][m] and\
                not self.grid[(i/3)*3+j/3][m]:
                #    print i,j,self.board
                    self.board[i][j]=str(m+1)
                    self.row[i][m]=True
                    self.col[j][m]=True
                    self.grid[(i/3)*3+j/3][m]=True
                    if j<8:
                        if self.dfs(i,j+1):
                            return True
                    else:
                        if self.dfs(i+1,0):
                            return True
                    self.board[i][j]='.'
                    self.row[i][m]=False
                    self.col[j][m]=False
                    self.grid[(i/3)*3+j/3][m]=False
        else:
            if j<8:
                if self.dfs(i,j+1):
                    return True
            else:
                if self.dfs(i+1,0):
                    return True


    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board=[[]for i in range(9)]
        for idx,item in enumerate(board):
            self.board[idx]=list(item)
        self.row=[[False for i in range(9)] for j in range(9)]
        self.col=[[False for i in range(9)] for j in range(9)]
        self.grid=[[False for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    self.row[i][ord(board[i][j])-ord('1')]=True
                    self.col[j][ord(board[i][j])-ord('1')]=True
                    self.grid[(i/3)*3+j/3][ord(board[i][j])-ord('1')]=True

        self.dfs(0,0)
        for idx,item in enumerate(board):
            board[idx]=''.join(self.board[idx])
        #print board
#
if __name__=="__main__":
    a=Solution()
    print a.solveSudoku\
    (["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])