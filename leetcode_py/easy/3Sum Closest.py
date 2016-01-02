class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                tmpres = nums[l] + nums[r] + nums[i]
                if abs(tmpres - target) < abs(result - target):
                    result = tmpres
                if tmpres < target:
                    l += 1
                elif tmpres > target:
                    r -= 1
                else:
                    return target
        return result


if __name__ == '__main__':
    a = Solution()
    print a.threeSumClosest([0, 2, 1, -3], 1)
    print a.threeSumClosest([1, 1, 1, 0], 100)
    print a.threeSumClosest([0, 0, 0], 2)
    print a.threeSumClosest([0, 1, 2], 3)
    print a.threeSumClosest([-1, 2, 1, 4], 1)
    print a.threeSumClosest([-1, 2, 3], 1)
