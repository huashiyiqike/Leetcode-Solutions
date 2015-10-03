
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        row=[[False for i in range(9)] for j in range(9)]
        col=[[False for i in range(9)] for j in range(9)]
        small=[[False for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num=ord(board[i][j])-ord('1')
                    k=(i/3)*3+(j/3)
                    if row[i][num] or col[j][num] or small[k][num]:
                        return False
                    else:
                        row[i][num]=True
                        col[j][num]=True
                        small[k][num]=True
        return True