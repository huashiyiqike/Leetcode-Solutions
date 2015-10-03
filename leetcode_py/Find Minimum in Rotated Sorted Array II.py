class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)/2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] <= nums[r]:
                r -= 1
        return nums[r+1]

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)/2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            elif nums[mid] == nums[r]:
                r -= 1
            if l == r and nums[l] == nums[r]:
                return nums[l]
        return nums[l]

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        low,high=0,len(num)-1
        while low<high:
            mid=(low+high)>>1
            if num[mid]>num[high]:
                low=mid+1
            elif num[mid]==num[high]:
                high-=1
            else:
                high=mid
        return num[low]