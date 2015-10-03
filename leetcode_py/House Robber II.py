class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = dp[1] = nums[0]
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        res = dp[-2]

        dp = [0] * len(nums)
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return max(res, dp[-1])




class Solution:
    def f(self, nums, start, end):
        dp = [0] * (end + 2 - start + 1)
        for i in range(end + 1 - start):
            dp[i+2] = max(dp[i] + nums[i+start], dp[i+1])
        return dp[-1]

    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.f(nums, 0, len(nums)-2), self.f(nums, 1, len(nums)-1))
