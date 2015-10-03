class Solution:
    def f(self,S,start,path,res):
        res.append(path)
        for i in range(start, len(S)):
            if i != start and S[i] == S[i-1]:
                continue
            self.f(S, i+1, path + [S[i]], res)

    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res=[]
        self.f(sorted(S),0,[],res)
        return res


class Solution:
    def f(self,S,start,path,res):
        if start > len(S)-1:
            if path not in res:
                res += [path]
            return

        self.f(S,start+1,path,res)
        self.f(S,start+1,path+[S[start]],res)

    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res=[]
        self.f(sorted(S),0,[],res)
        return res

class Solution:
    def helper(self, nums, res, path, idx):
        if idx >= len(nums):
            res.append(path)
            return
        self.helper(nums, res, path + [nums[idx]], idx+1)
        if not path or path[-1] != nums[idx]:
            self.helper(nums, res, path, idx+1)

    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        res = []
        self.helper(sorted(nums), res, [], 0)
        return res
