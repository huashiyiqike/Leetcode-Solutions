class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ResGrid = [[0 for x in range(n + 1)] for x in range(m + 1)]
        ResGrid[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not obstacleGrid[i - 1][j - 1]:
                    ResGrid[i][j] = ResGrid[i][j - 1] + ResGrid[i - 1][j]

        return ResGrid[m][n]


class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        res = [[0] * len(obstacleGrid[0])] * len(obstacleGrid)
        for idx, item in enumerate(obstacleGrid):
            for idy, a in enumerate(item):
                if a == 1:
                    res[idx][idy] = 0
                elif idx == 0 and idy == 0:
                    res[0][0] = 1
                elif idx == 0:
                    res[idx][idy] = res[idx][idy - 1]
                elif idy == 0:
                    res[idx][idy] = res[idx - 1][idy]
                else:
                    res[idx][idy] = res[idx - 1][idy] + res[idx][idy - 1]
        return res[-1][-1]


if __name__ == "__main__":
    a = Solution()
    print a.uniquePathsWithObstacles([[1, 0]])
