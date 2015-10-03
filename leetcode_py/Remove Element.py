class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        idx = 0
        for i in nums:
            if i != val:
                nums[idx] = i
                idx += 1
        return idx


