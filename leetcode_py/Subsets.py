class Solution:
    def helper(self, res, path, nums, idx):
        res.append(path)
        for i in range(idx, len(nums)):
            self.helper(res, path+[nums[i]], nums, i+1)

    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        res = []
        self.helper(res, [], sorted(nums), 0)
        return res

class Solution:
    def helper(self, res, path, idx, nums):
        if idx == len(nums):
            res.append(path)
            return
        self.helper(res, path, idx+1, nums)
        self.helper(res, path+[nums[idx]], idx+1, nums)

    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        res = []
        self.helper(res, [], 0, sorted(nums))
        return res

import datetime
# dp
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        res=[[]]
        for i in nums:
            tmp = res[:]
            for j in res:
                tmp.append(j + [i])
            res = tmp
        return res

