class Solution:
    def helper(self, n, k, idx, res, path):
        if len(path) == k:
            res.append(path)
            return
        for i in range(idx, n + 1):
            self.helper(n, k, i + 1, res, path + [i])

    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        res = []
        self.helper(n, k, 1, res, [])
        return res



class Solution:
    def helper(self, n, k, idx, path):
        if len(path) == k:
            return [path]
        if idx > n:
            return []

        return self.helper(n, k, idx + 1, path + [idx]) + self.helper(n, k, idx + 1, path)

    # @param {integer[]} nums
    # @return {integer[][]}
    def combine(self, n, k):
        return self.helper(n, k, 1, [])

class Solution:
    def helper(self, n, k, idx, res, path):
        if len(path) == k:
            res.append(path)
            return
        if idx > n:
            return

        self.helper(n, k, idx + 1, res, path + [idx])
        self.helper(n, k, idx + 1, res, path)

    # @param {integer[]} nums
    # @return {integer[][]}
    def combine(self, n, k):
        res = []
        self.helper(n, k, 1, res, [])
        return res

class Solution:
    def find(self, limit, res, path, remain_count, pos):
        if remain_count == 0:
            res.append(path)
            return
        for i in range(pos,limit):
            self.find(limit, res, path + [i], remain_count - 1, i+1)
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        res = []
        self.find(n+1, res, [], k, 1)
        return res
