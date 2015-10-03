class Solution(object):
    def helper(self, nums, l, r):
        if l == r:
            return r
        mid = (l+r) / 2
        idx1, idx2 = self.helper(nums, l, mid), self.helper(nums, mid+1, r)
        return idx1 if nums[idx1] > nums[idx2] else idx2

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)

if __name__ == "__main__":
    a = Solution()
    a.findPeakElement([3,2,1])


class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        nums = [-1<<64] + nums + [-1<<64]
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)/2
            a, b, c = nums[mid-1], nums[mid], nums[mid+1]
            if a < b > c:
                return mid - 1
            elif a < b < c:
                l = mid
            elif a > b > c:
                r = mid
            elif a > b < c:
                l = mid


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        left = 1
        right = len(num)
        num = [-2 ** 64] + num + [-2 ** 64]
        while left <= right:
            mid = (left + right) / 2
            if num[mid - 1] < num[mid] < num[mid + 1]:
                left = mid + 1
            elif num[mid - 1] > num[mid] > num[mid + 1]:
                right = mid - 1
            elif num[mid - 1] < num[mid] > num[mid + 1]:
                return mid - 1
            else:
                right = mid


