class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums.sort()
        res = set([])
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                dict = {}
                for k in range(j+1, len(nums)):
                    if nums[k] in dict:
                        res.add((nums[i], nums[j], nums[dict[nums[k]]], nums[k]))
                    else:
                        dict[target-nums[k]-nums[i]-nums[j]] = k
        return map(list, res)


class Solution:
    def twosum(self,nums,target,res,idx1,idx2):
        dicts={}
        for i in range(idx2+1,len(nums)):
            if nums[i] in dicts:
                res.add((nums[idx1],nums[idx2],nums[dicts[nums[i]]],nums[i]))
            else:
                dicts[target-nums[i]]=i


    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums.sort()
        res=set([])
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                self.twosum(nums,target-nums[i]-nums[j],res,i,j)
                # return list(res)
        r=[]
        for i in res:
            r.append(list(i))
        return r


