class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        for idx, item in enumerate(nums):
            if nums[idx] in dict and idx - dict[nums[idx]] <= k:
                return True
            dict[nums[idx]] = idx
        return False

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        sets = set([])
        for i in range(min(k, len(nums))):
            if nums[i] in sets:
                return True
            else:
                sets.add(nums[i])
        for i in range(k, len(nums)):
            if nums[i] in sets:
                return True
            else:
                sets.add(nums[i])
                sets.remove(nums[i-k])
        return False

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if k<=0:
            return False
        sets=set([])

        for i in range(k):
            if i > len(nums)-1:
                return False
            if nums[i] in sets:
                return True
            else:
                sets.add(nums[i])

        for i in range(k,len(nums)):
            if nums[i] in sets:
                return True
            else:
                sets.add(nums[i])
            sets.remove(nums[i-k])

        return False


