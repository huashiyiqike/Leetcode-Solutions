class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in xrange(n)] for i in xrange(m)]

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0

        ans = max([max(i) for i in dp])
        return ans ** 2


class Solution:
    def check(self, m, i, j):
        left = max(0, j - m[i][j] + 1)
        pos = j
        mins = m[i][j]
        res = 0
        while left < pos:
            pos -= 1
            if pos < 0:
                break
            if m[i][pos] < mins:
                mins = m[i][pos]
                left = max(0, j - m[i][pos])
            res = max(res, min(mins, (j - pos + 1)) ** 2)
        return res

    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m = [[0] * len(matrix[0]) for _ in matrix]
        res = 0
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                m[i][j] = int(matrix[i][j])
                if m[i][j] != 0:
                    res = 1
                    if i > 0:
                        m[i][j] = m[i - 1][j] + 1
        if res == 0:
            return 0
            #  print m
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if m[i][j] > 1:
                    res = max(res, self.check(m, i, j))
                    # print i, j, res
        return res


if __name__ == '__main__':
    a = Solution()
    print a.maximalSquare(["1101", "1101", "1111"])
    print a.maximalSquare(["01101", "11010", "01110", "11110", "11111", "00000"])
    print a.maximalSquare([[1, 1], [1, 1]])
    print a.maximalSquare(
        [[1, 0, 1, 0, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0]])
