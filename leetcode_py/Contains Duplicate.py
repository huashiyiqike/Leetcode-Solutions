class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        sets=set([])
        for i in nums:
            if i in sets:
                return True
            else:
                sets.add(i)
        return False