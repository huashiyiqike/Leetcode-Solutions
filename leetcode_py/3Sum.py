class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        res = []
        for idx, item in enumerate(nums):
            if idx > 0 and item == nums[idx - 1]:
                continue
            target = -item
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                tmp = nums[left] + nums[right]
                if tmp < target:
                    left += 1
                elif tmp > target:
                    right -= 1
                else:
                    res.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
        return res


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < -nums[i]:
                    left += 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left + 1 < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                        # if (left == i+1 or nums[left] != nums[left-1]) and \
                        #         (right == len(nums)-1 or nums[right] != nums[right+1]):
                        #     res.append([nums[i], nums[left], nums[right]])
                        #     left += 1
                        #     right -= 1
                        # elif left > i+1 and nums[left] == nums[left-1]:
                        #     left += 1
                        # elif right < len(nums)-1 and nums[right] == nums[right+1]:
                        #     right -= 1
        return res


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def find(self, lists, aim, out, resultlist):
        dic = {}
        for item in lists:
            if item not in dic:
                dic[aim - item] = item

            else:
                res = [out, dic[item], item]
                if res not in resultlist:
                    resultlist.append(res)

    def threeSum(self, num):
        resultlist = []
        num = sorted(num)
        for idx, item in enumerate(num):
            self.find(num[idx + 1:], -item, item, resultlist)
        return resultlist


if __name__ == '__main__':
    a = Solution()
    print a.threeSum([0])
    print a.threeSum([-1, -1, 2, 1, 1, 0])
    print a.threeSum([-1, 0, 1])

# https://leetcode.com/discuss/23595/share-my-solution-around-50ms-with-explanation-and-comments
