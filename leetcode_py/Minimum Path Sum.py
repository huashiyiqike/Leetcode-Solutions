class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        dp = [[1 << 64] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
        dp[0][1] = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        res = [[0] * len(grid[0])] * len(grid)
        res[0][0] = grid[0][0]
        for idx, item in enumerate(grid):
            for idy, a in enumerate(item):
                if idy == 0 and idx > 0:
                    res[idx][idy] = res[idx - 1][idy] + grid[idx][idy]
                elif idx == 0 and idy > 0:
                    res[idx][idy] = res[idx][idy - 1] + grid[idx][idy]
                elif idx > 0 and idy > 0:
                    res[idx][idy] = min(res[idx - 1][idy], res[idx][idy - 1]) + grid[idx][idy]
        return res[-1][-1]
