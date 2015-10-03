import math
import sys

# static dp, saves dp matrices for different test cases
class Solution(object):
    _f = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = self._f
        while len(f) <= n:
            temp = f[-1]
            j = 1
            while j * j <= len(f):
                temp = min(temp, f[-j * j])
                j += 1
            f.append(temp + 1)
        return f[n]

# normal dp TLE
# import sys
# class Solution(object):
#     def numSquares(self, n):
#         dp = [0]
#         for i in range(n + 1):
#             dp.append(sys.maxint)
#             for j in range(1, int(math.sqrt(i)) + 1):
#                 dp[i] = min(dp[i], dp[i - j * j] + 1)
#         return dp[n]


class Solution(object):
    _dp = [0]

    def numSquares(self, n):
        dp = self._dp
        while n >= len(dp):
            tmp = sys.maxint
            for j in range(1, int(math.sqrt(len(dp))) + 1):
                tmp = min(tmp, dp[-j * j] + 1)
            dp.append(tmp)
        return dp[n]


if __name__ == '__main__':
    a = Solution()
    print a.numSquares(1)
    print a.numSquares(223)
    print a.numSquares(12)
    print a.numSquares(15351)


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = [n]
        step = 0
        while queue:
            next = []
            while queue:
                start = queue.pop(0)
                for i in range(int(math.sqrt(start)), 0, -1):
                    var = i * i
                    if var == start:
                        return step + 1
                    next.append(start - var)
            step += 1
            queue = next


if __name__ == '__main__':
    a = Solution()
    print a.numSquares(223)
    print a.numSquares(12)
    print a.numSquares(15351)
