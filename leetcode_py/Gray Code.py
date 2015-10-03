
class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        res=[0]
        for i in range(n):
            tmpres = res[:]
            for j in res[::-1]:
                tmpres.append(j + 2 ** i)
            res = tmpres
        return res

class Solution:
    def str2int(self, str):
        res = 0
        for i in range(len(str)):
            res <<= 1
            if str[i] == '1':
                res += 1
        return res

    def helper(self, n):
        if n == 1:
            return ['0', '1']
        elif n > 1:
            tmp = self.helper(n-1)
            return map(lambda x: '0'+x, tmp) + map(lambda x: '1'+x, tmp[::-1])

    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        if n == 0:
            return [0]
        res = self.helper(n)
        return map(self.str2int, res)




class Solution:
    def dif1(self, a, b):
        tmp = a^b
        if tmp and not (tmp & (tmp-1) ):
            return True
        return False
    def next(self, n, has, start):
        i = 0
        while i <= n:
            tmp = start
            tmp ^= 2**i
            if tmp not in has:
                if self.dif1(tmp, start):
                    has.add(tmp)
                    return tmp
            i += 1

    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        res = [0]
        has = set(res)
        for i in range(2**n-1):
            res.append(self.next(n, has, res[-1]))
        return res
if __name__=="__main__":
    a=Solution()
    print a.grayCode(3)




class Solution:
    def f(self,l):
        tmp=0
        for i in range(len(l)):
            tmp<<=1
            tmp+=l[i]
        return tmp

    def grayCode(self, n):
        if n==0:
            return [0]
        res=[[0],[1]]
        for i in range(n-1):
            path1,path2=[],[]
            for idx in range(len(res)):
                path1.append([0]+res[idx])
                path2.append([1]+res[len(res)-1-idx])
            res=path1+path2
        for idx in range(len(res)):
            res[idx]=self.f(res[idx])
        return res


class Solution:
    def f(self,n):
        if n==1:
            return [0]
        tmp=self.f(n-1)
        return tmp+[n-1]+tmp
    # @return a list of integers
    def grayCode(self, n):
        if n==0:
            return [0]
        lists=self.f(n)
        res=[0]
        for i in lists:
            res.append(res[-1]^(1<<i))
        return res

if __name__=="__main__":
    a=Solution()
    print a.grayCode(3)

