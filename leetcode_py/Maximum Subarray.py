import sys
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        lo = glo = - sys.maxint
        for i in nums:
            lo = max(lo + i, i)
            glo = max(lo, glo)
        return glo


if __name__ == '__main__':
    import sys

    a = Solution()
    if len(sys.argv) == 1:
        print a.maxSubArray([1, 2, 3, -2, 3])
    else:
        print a.maxSubArray(sys.argv[1])
