class Solution:
    # @param nums, a list of integer 
    # @param k, num of steps 
    # @return nothing, please modify the nums list in-place. 
    def f(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums, k):
        k %= len(nums)
        if k == 0:
            return
        self.f(nums, 0, len(nums) - k - 1)
        self.f(nums, len(nums) - k, len(nums) - 1)
        self.f(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    a = Solution()
    num = [1, 2, 3, 4, 5, 6]
    a.rotate(num, 4)
    print num
