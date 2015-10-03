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
            else:
                return nums[mid]
        return nums[l]

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l=0
        r=len(num)-1
        while l<r:
            mid=(l+r)>>1
            if num[mid]>=num[r]:
                l=mid+1
            else:
                r=mid

        return num[l]

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l=0
        r=len(num)-1
        while l<=r:
            mid=(l+r)>>1
            if num[mid]>=num[0]:
                l=mid+1
            else:
                r=mid-1
        if l>len(num)-1:
            return num[0]
        else:
            return num[l]