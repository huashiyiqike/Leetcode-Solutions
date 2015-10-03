class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        res = 1
        m = abs(n)
        while m:
            if m&1:
                res *= x
            m >>= 1
            x *= x
        if n < 0:
            res = 1/res
        return res

