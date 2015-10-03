class Solution:
    def helper(self, candidates, target, start, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(start, len(candidates)):
            if target - candidates[start] >= 0:
                self.helper(candidates, target - candidates[i], i, path + [candidates[i]], res)
            else:
                return

    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        res = []
        self.helper(sorted(candidates), target, 0, [], res)
        return res
