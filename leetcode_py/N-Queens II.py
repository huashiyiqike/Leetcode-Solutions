from collections import defaultdict
class Solution:
    def helper(self, viscol, vissum, vismis, row, total, res):
        for i in range(total):
            if not viscol[i] and not vissum[row+i] and not vismis[row-i]:
                if row == total-1:
                    res[0] += 1
                else:
                    viscol[i] = True
                    vissum[row+i] = True
                    vismis[row-i] = True
                    self.helper(viscol, vissum, vismis, row+1, total, res)
                    viscol[i] = False
                    vissum[row+i] = False
                    vismis[row-i] = False


    # @param {integer} n
    # @return {string[][]}
    def totalNQueens(self, n):
        viscol = defaultdict(bool)
        vissum = defaultdict(bool)
        vismis = defaultdict(bool)
        res = [0]
        self.helper(viscol, vissum, vismis, 0, n, res)
        return res[0]


class Solution:
    def f(self, n, x, rows, cols, row_col, col_row):
        if x == n:
            self.res += 1
        for y in range(n):
            if 2 ** x & rows or 2 ** y & cols or 2 ** (n+x-y) & row_col or 2 ** (y+x) & col_row:
                continue
            rows |= 2 ** x
            cols |= 1 << y
            row_col |= 1 << (n+x-y)
            col_row |= 1 << (y+x)
            self.f(n, x+1, rows, cols, row_col, col_row)
            rows &= ~ 2 ** x
            cols &= ~ (1 << y)
            row_col &= ~ 2 ** (n+x-y)
            col_row &= ~ 2 ** (x+y)

    # @param {integer} n
    # @return {string[][]}
    def totalNQueens(self, n):
        self.res = 0
        self.f(n, 0, 0, 0, 0, 0)
        return self.res

if __name__=="__main__":
    a=Solution()
    tmp=a.totalNQueens(12)  
    print tmp
#     for i in tmp:
#         print i
    