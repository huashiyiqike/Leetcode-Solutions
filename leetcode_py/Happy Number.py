class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        sets={n}
        while n != 1:
            tmp=n
            res=0
            while tmp > 0:
                res += (tmp % 10)**2
                tmp /= 10
            n=res
            if n in sets:
                return False
            sets.add(n)
        return True
