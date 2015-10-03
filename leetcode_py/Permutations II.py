class Solution:
    def helper(self, nums, res, path, vis):
        if len(path) == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and vis[i-1]:
                continue
            if not vis[i]:
                vis[i] = True
                self.helper(nums, res, path + [nums[i]], vis)
                vis[i] = False

    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        nums = sorted(nums)
        res = []
        vis = [False] * len(nums)
        self.helper(nums, res, [], vis)
        return res


# this can be same as leetcode Permutaitons
class Solution:
    def next(self, cur):
        for j in range(len(cur)-2, -1, -1):
            for i in range(len(cur)-1, j, -1):
                if cur[i] > cur[j]:
                    cur[i], cur[j] = cur[j], cur[i]
                    cur[j+1:] = cur[j+1:][::-1]
                    return cur
        return False

    def permuteUnique(self, num):
        num = sorted(num)
        res = [num[::]]
        while num:
            num = self.next(num)
            if num:
                res.append(num[::])
        return res

