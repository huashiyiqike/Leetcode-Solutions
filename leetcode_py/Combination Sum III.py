class Solution:
    def helper(self, k, target, start, path, res):
        if len(path) == k and target == 0:
            res.append(path)
        for i in range(start, 10):
            if target - i >= 0:
                self.helper(k, target - i, i + 1, path + [i], res)
            else:
                return

    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        res = []
        self.helper(k, n, 1, [], res)
        return res


class Solution:
    def find(self, nums, target, remain_count, pos, res, path):
        if target == 0 and remain_count == 0:
            res.append(path)
            return
        if pos > 9 or remain_count <= 0:
            return

        for i in range(pos, len(nums)):
            if nums[i] > target:
                break
            self.find(nums, target - nums[i], remain_count - 1, i + 1, res, path + [nums[i]])

    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        res = []
        self.find(range(1, 10), n, k, 0, res, [])
        return res


class Solution:
    def f(self, k, start, n, path):
        if n == 0 and k == 0:
            self.res.append(path)
            return
        elif n <= 0 or k <= 0 or start >= 10:
            return
        self.f(k - 1, start + 1, n - start, path + [start])
        self.f(k, start + 1, n, path)

    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        self.res = []
        self.f(k, 1, n, [])
        return self.res
