import math
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        cur = 5
        res = 0
        while cur <= n:
            res += n/cur
            cur *= 5
        return res

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        if n==0:
            return 0
        a=int(math.log(n,5))
        res=0
        for i in xrange(1,a+1):
            res+=int(n/(5**i))

        return res

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        if n==0:
            return 0
        a=int(math.log(n,5))
        res=0
        for i in xrange(a,0,-1):
            res+=i*int(n/(5**i))
        for i in xrange(a-1,0,-1):
            res-=i*int(n/5**(i+1))
        return res
    
if __name__=="__main__":
    a=Solution()
    for i in range(1,126):
        print a.trailingZeroes(i)
