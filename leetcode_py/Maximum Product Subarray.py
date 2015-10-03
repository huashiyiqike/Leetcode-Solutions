class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        dpmax = nums[:]
        dpmin = nums[:]
        res = nums[0]
        for idx, item in enumerate(nums[1:], start=1):
            dpmax[idx] = max(dpmax[idx - 1] * item, dpmin[idx - 1] * item, item)
            dpmin[idx] = min(dpmax[idx - 1] * item, dpmin[idx - 1] * item, item)
            res = max(res, dpmax[idx])
        return res


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if not nums:
            return 0

        res = pos = neg = nums[0]
        for i in nums[1:]:
            neg *= i
            pos *= i
            tmp = pos
            pos = max(neg, i, pos)
            neg = min(neg, i, tmp)
            res = max(res, pos)
            # print pos, neg
        return res


if __name__ == "__main__":
    a = Solution()
    print a.maxProduct([0, 2])
    print a.maxProduct([-2, 3, -4])
    print a.maxProduct([-2, 2, -2, 0, -2, -3, -5, -2])
    print a.maxProduct([3, -1, 4])
    print a.maxProduct([-2, 0, -1])
    print a.maxProduct([2, -5, -2, -4, 3])
# from operator import neg
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 1:
            return A[0]

        pos = A[0]
        neg = A[0]
        maxx = pos
        for i in A[1:]:
            tmp = pos
            pos = max(i * pos, i, i * neg)
            neg = min(i * tmp, i, i * neg)
            maxx = max(pos, maxx)
        return maxx


if __name__ == "__main__":
    a = Solution()
    print a.maxProduct([-2, 2, -2, 0, -2, -3, -5, -2])
    print a.maxProduct([3, -1, 4])
    print a.maxProduct([-2, 0, -1])
    print a.maxProduct([2, -5, -2, -4, 3])
