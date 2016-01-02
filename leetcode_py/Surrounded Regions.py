import sys

sys.setrecursionlimit(100000)


class Solution:
    def setm(self, board, i, j):
        board[i][j] = 'm'
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d in dirs:
            idx = i + d[0]
            idy = j + d[1]
            if 0 < idx < len(board) - 1 and 0 < idy < len(board[0]) - 1 and board[idx][idy] == 'O':
                self.setm(board, idx, idy)  # no boarder involved for recursion depth

    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == len(board) - 1 or j == len(board[0]) - 1 or j == 0) \
                        and board[i][j] == 'O':
                    self.setm(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'm':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


# iterative recursive depth first search, only start from outer circles
class Solution:
    def solve(self, board):
        if len(board) == 0:
            return
        visited = {}
        stack = [(i, j) for i in range(len(board)) for j in (0, len(board[0]) - 1)]
        stack += [(i, j) for i in (0, len(board) - 1) for j in range(len(board[0]))]

        while stack:
            i, j = stack.pop()
            visited[(i, j)] = True
            if board[i][j] == 'O':
                board[i][j] = 'V'
                for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) \
                            and (x, y) not in visited:
                        visited[(x, y)] = True
                        stack.append((x, y))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


# recersive depth search
class Solution:
    def explore(self, grid, x, y):
        grid[x][y] = 'U'
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in dir:
            tmpx = x + i[0]
            tmpy = y + i[1]
            if tmpx > 0 and tmpx < len(grid) - 1 and tmpy > 0 and tmpy < len(grid[0]) - 1:
                if grid[tmpx][tmpy] == 'O':
                    self.explore(grid, tmpx, tmpy)

    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        for idx in range(len(board)):
            for idy in range(len(board[0])):
                if (idx == 0 or idx == len(board) - 1 or idy == 0 or idy == len(board[0]) - 1) and board[idx][
                    idy] == 'O':
                    self.explore(board, idx, idy)
                    #   print board
        for idx, item in enumerate(board):
            for idy, x in enumerate(item):
                if board[idx][idy] == 'U':
                    board[idx][idy] = 'O'
                elif board[idx][idy] == 'O':
                    board[idx][idy] = 'X'
                    #   print board


if __name__ == "__main__":
    a = Solution()
    board = [['O']]
    a.solve(board)
    print board
