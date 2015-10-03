class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        nums = set(nums)
        res = 0
        while nums:
            len = 1
            pre = after = nums.pop()
            while pre - 1 in nums:
                nums.remove(pre - 1)
                len += 1
                pre -= 1
            while after + 1 in nums:
                nums.remove(after + 1)
                len += 1
                after += 1
            res = max(res, len)
        return res



class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        nums=set(nums)
        res=0
        while nums:
            pre=after=nums.pop()
            lens=1
            while pre-1 in nums:
                nums.remove(pre-1)
                lens+=1
                pre-=1
            while after+1 in nums:
                nums.remove(after+1)
                after+=1
                lens+=1
            res=max(res,lens)
        return res


class Solution:
    def f(self,left,right,maps):
        lower=left-maps[left]+1
        upper=right+maps[right]-1
        lens=upper-lower+1
        maps[lower]=lens
        maps[upper]=lens
        return lens

    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        maps={}
        res=1
        for i in num:
            if i in maps:
                continue
            maps[i]=1
            if i+1 in maps:
                res=max(res,self.f(i,i+1,maps))
            if i-1 in maps:
                res=max(res,self.f(i-1,i,maps))

        return res

if __name__=="__main__":
    a=Solution()
    print a.longestConsecutive([1,2,3,4,555,6,5,200])

# TLE
from collections import defaultdict
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        dict = defaultdict(int)
        res = 0
        for i in nums:
            if i not in dict:
                if i - 1 in dict:
                    dict[i] = dict[i-1] + 1
                    res = max(res, dict[i])
                    while i-1 in dict:
                        dict[i-1] = dict[i]
                        i -= 1
                elif i + 1 in dict:
                    dict[i] = dict[i+1] + 1
                    res = max(res, dict[i])
                    while i + 1 in dict:
                        dict[i+1] = dict[i]
                        i += 1
                else:
                    dict[i] = 1
                    res = max(res, 1)
        return res

