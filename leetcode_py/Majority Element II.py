class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in set([candidate1, candidate2]) if nums.count(n) > len(nums) // 3]

from collections import defaultdict
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        dict = defaultdict(int)
        for i in nums:
            if i in dict or len(dict)<3:
                dict[i] += 1
            else:
                for key, value in dict.items():
                    if value == 0:
                        dict.pop(key)
                    else:
                        dict[key] -= 1
        for key in dict:
            dict[key] = 0
        for i in nums:
            if i in dict:
                dict[i] += 1
        res = []
        for key, value in dict.items():
            if value > len(nums)/3:
                res.append(key)
        return res


if __name__ == '__main__':
    a = Solution()
    print a.majorityElement([-1,100,2,100,100,4,100])
    print a.majorityElement([1,2,3])
    print a.majorityElement([1,2,0,4,5,0,6,7,8,9,9,9,9,9,9,0,0,0,0,0])