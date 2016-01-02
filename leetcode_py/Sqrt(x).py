class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = (left + right) / 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        return right


class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return 0
        left, right = 1, x
        while left < right - 1:
            mid = (left + right) / 2
            tmp = mid * mid
            if tmp < x:
                left = mid
            elif tmp > x:
                right = mid - 1
            else:
                return mid
        if right * right <= x:
            return right
        else:
            return left
