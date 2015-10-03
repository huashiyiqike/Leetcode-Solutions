# knows the end, so dp backwards
class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        dp = [[None] * len(dungeon[0]) for _ in dungeon]
        rows = len(dungeon)-1
        cols = len(dungeon[0])-1
        for i in range(rows, -1, -1):
            for j in range(cols, -1, -1):
                if i == rows and j == cols:
                    dp[i][j] = max(0, -dungeon[i][j])
                elif i == rows:
                    dp[i][j] = max(0, dp[i][j+1]-dungeon[i][j])
                elif j == cols:
                    dp[i][j] = max(0, dp[i+1][j]-dungeon[i][j])
                else:
                    dp[i][j] = min(max(0, dp[i][j+1]-dungeon[i][j]), max(0, dp[i+1][j]-dungeon[i][j]))
                    # dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 0)
        return dp[0][0] + 1
