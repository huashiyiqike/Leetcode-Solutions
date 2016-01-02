class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        idx2, idx3, idx5 = 0, 0, 0
        for i in range(n - 1):
            res.append(min(res[idx2] * 2, res[idx3] * 3, res[idx5] * 5))
            if res[-1] == res[idx2] * 2:
                idx2 += 1
            if res[-1] == res[idx3] * 3:
                idx3 += 1
            if res[-1] == res[idx5] * 5:
                idx5 += 1
        return res[-1]


if __name__ == "__main__":
    a = Solution()
    print a.nthUglyNumber(7)
