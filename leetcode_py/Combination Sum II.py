class Solution:
    def helper(self, candidates, target, start, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(start, len(candidates)):
            if target - candidates[start] >= 0:
                if i != start and candidates[i] == candidates[i-1]:
                    continue
                self.helper(candidates, target - candidates[i], i+1, path + [candidates[i]], res)
            else:
                return

    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        res = []
        self.helper(sorted(candidates), target, 0, [], res)
        return res

class Solution:
    def helper(self, candidates, target, start, path, res):
        if target == 0:
            if path not in res: # slow
                res.append(path)
            return
        for i in range(start, len(candidates)):
            if target - candidates[start] >= 0:
                self.helper(candidates, target - candidates[i], i+1, path + [candidates[i]], res)
            else:
                return

    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        res = []
        self.helper(sorted(candidates), target, 0, [], res)
        return res


#TLE
class Solution:
    def find(self, candidates, target, res, path, pos):
        if target == 0:
            res.append(path)
            return
        if target <0 or pos >= len(candidates) or candidates[pos]>candidates:
            return
        self.find(candidates, target, res, path, pos + 1)
        self.find(candidates, target - candidates[pos], res, path + [candidates[pos]], \
                  pos + 1)

    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        res=[]
        self.find(sorted(candidates), target, res, [], 0)
