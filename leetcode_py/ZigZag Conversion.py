class Solution:
    def convert(self, s, nRows):
        step, zigzag = 2 * nRows - 2, ""
        if not s or len(s) == 0 or nRows <= 0:
            return ""
        if nRows == 1:
            return s
        for i in range(nRows):
            for j in range(i, len(s), step):
                zigzag += s[j]
                if 0 < i < nRows - 1 and j + step - 2 * i < len(s):
                    zigzag += s[j + step - 2 * i]
        return zigzag


class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        res = ''
        n = nRows
        d1 = 2 * n - 2

        idx = 0
        while idx < len(s):
            res += s[idx]
            idx += d1

        for i in range(1, n - 1):
            idx1 = i
            idx2 = -i
            m = idx1
            j = 0
            while m < len(s):
                res += s[m]
                if j % 2 == 0:
                    idx2 += 2 * n - 2
                    m = idx2
                else:
                    idx1 += 2 * n - 2
                    m = idx1
                j += 1
        idx = n - 1
        while idx < len(s):
            res += s[idx]
            idx += d1
        return res


if __name__ == "__main__":
    a = Solution()
    print a.convert("PAYA", 3)
    # should return "PAHNAPLSIIGYIR"'
