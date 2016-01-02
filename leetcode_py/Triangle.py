class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        res = [[0 for i in j] for j in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for idx, item in enumerate(res[i]):
                if idx == 0:
                    res[i][0] = res[i - 1][0] + triangle[i][0]
                elif idx == len(res[i]) - 1:
                    res[i][idx] = res[i - 1][idx - 1] + triangle[i][idx]
                else:
                    res[i][idx] = min(res[i - 1][idx - 1] + triangle[i][idx], res[i - 1][idx] + triangle[i][idx])
        # print res
        return min(res[-1])


if __name__ == "__main__":
    a = Solution()
    print  a.minimumTotal([[1], [2, 3]])
    print  a.minimumTotal([[-1], [-2, -3]])
    print  a.minimumTotal([[-1], [2, 3], [1, -1, -1]])
