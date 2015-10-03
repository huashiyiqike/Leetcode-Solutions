class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (0+len(nums)) * (len(nums)+1) / 2 - sum(nums)

# binary search
class Solution(object):
    # find the first less than its index
    def missingNumber(self, nums):
        nums.sort()
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)/2
            if nums[mid] == mid:
                left = mid + 1
            elif nums[mid] > mid:
                right = mid - 1
        return left