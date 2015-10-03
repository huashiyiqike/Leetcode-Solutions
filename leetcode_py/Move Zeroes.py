class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                nums[idx] = nums[i]
                idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0