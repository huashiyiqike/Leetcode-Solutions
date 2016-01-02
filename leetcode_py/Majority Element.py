class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        count = 0
        maj = nums[0]
        for idx, item in enumerate(nums):
            if item == maj:
                count += 1
            else:
                count -= 1
                if count < 0:
                    maj = item
                    count = 0
        return maj


class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        num = sorted(num)
        return num[len(num) / 2]
