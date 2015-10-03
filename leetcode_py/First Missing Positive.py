class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        idx = 0
        while idx < len(nums):
            if 0 < nums[idx] <= len(nums) and nums[idx] != nums[nums[idx]-1]:
                tmp = nums[nums[idx]-1]
                nums[nums[idx]-1] = nums[idx]
                nums[idx] = tmp
            else:
                idx += 1
        for idx, item in enumerate(nums):
            if idx+1 != item:
                return idx + 1
        return len(nums)+1

class Solution(object):
    import sys
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        while idx < len(nums):
            tmp = nums[idx]
            count = 0
            while 0 < tmp <= len(nums) and count < len(nums):
                newtmp = nums[tmp-1]
                nums[tmp-1] = tmp
                tmp = newtmp
                count += 1

            idx += 1
            #  print nums
        for idx, item in enumerate(nums):
            if item != idx+1:
                return idx+1
        return len(nums)+1

