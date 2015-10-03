from collections import defaultdict
class Solution:
    def helper(self, viscol, vissum, vismis, row, total, res, path):
        for i in range(total):
            if not viscol[i] and not vissum[row+i] and not vismis[row-i]:
                tmp = '.' * i + 'Q' + '.' * (total-1-i)
                if row == total-1:
                    res.append(path + [tmp])
                else:
                    viscol[i] = True
                    vissum[row+i] = True
                    vismis[row-i] = True
                    self.helper(viscol, vissum, vismis, row+1, total, res, path + [tmp])
                    viscol[i] = False
                    vissum[row+i] = False
                    vismis[row-i] = False


    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        viscol = defaultdict(bool)
        vissum = defaultdict(bool)
        vismis = defaultdict(bool)
        res = []
        path = []
        self.helper(viscol, vissum, vismis, 0, n, res, path)
        return res


class Solution:
    def f(self, n, res, path, x, rows, cols, row_col, col_row):
        if x == n:
            tmpres = []
            for i in path:
                tmpres.append(''.join(i))
            res.append(tmpres)
            return
        for y in range(n):
            if 2 ** x & rows or 2 ** y & cols or 2 ** (n+x-y) & row_col or 2 ** (y+x) & col_row:
                continue
            path[x][y] = 'Q'
            rows |= 2 ** x
            cols |= 1 << y
            row_col |= 1 << (n+x-y)
            col_row |= 1 << (y+x)
            self.f(n, res, path, x+1, rows, cols, row_col, col_row)
            path[x][y] = '.'
            rows &= ~ 2 ** x
            cols &= ~ (1 << y)
            row_col &= ~ 2 ** (n+x-y)
            col_row &= ~ 2 ** (x+y)

    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        res = []
        path = [['.']*n for _ in range(n)]
        print path
        self.f(n, res, path, 0, 0, 0, 0, 0)
        return res

if __name__=="__main__":
    a=Solution()
    tmp=a.solveNQueens(4)
    print len(tmp)
    for i in tmp:
        print i
#
# why? 1 dimension safe?
# #http://www.iteye.com/topic/106747
# bit manipulation
class Solution:
    def dfs(self,num,res,n):
        if num==n:
            tmp=[]
            for idx,item in enumerate(res):
                tmp.append(''.join(res[idx]))
            self.result.append(tmp)
        else:
            for i in range(n):
                tmp=1<<i
                tmprow_col=1<<(num-i+n)
                tmprowpcol=1<<(num+i)
                if not (self.rows&tmp) and not(self.col&tmp) and not(self.row_col&tmprow_col) \
                and not(self.rowpcol&tmprowpcol):
                    res[num][i]='Q'
                    self.rows|=tmp  
                    self.col|=tmp
                    self.row_col|=tmprow_col
                    self.rowpcol|=tmprowpcol
                    self.dfs(num+1,res,n)
                    
                    res[num][i]='.'
                    tmp=~tmp#(1<<i)#(1<<32)- (1<<i) - 1
                    tmprow_col=~tmprow_col#(1<<(num-i+n))#(1<<32)-(1<<((num-i+n)))-1
                    tmprowpcol=~tmprowpcol#(1<<(num+i))#(1<<32)-(1<<(num+i))-1
                    self.rows&=tmp 
                    self.col&=tmp 
                    self.row_col&=tmprow_col
                    self.rowpcol&=tmprowpcol
                    
                     
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.rows=0
        self.col=0
        self.row_col=0
        self.rowpcol=0
        self.result=[]
        res= [ [ '.' for i in range(n)] for j in range(n)]
        self.dfs(0,res,n)
        return self.result
        
if __name__=="__main__":
    a=Solution()
    tmp=a.solveNQueens(4)
    for i in tmp:
        print i