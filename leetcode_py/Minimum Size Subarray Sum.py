# binary search
class Solution:
    def bisearch(self, l, r, target, nums):
        while l <= r:
            mid = (l + r)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return r

    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        sums = nums
        res = 1 << 64
        for idx in range(1, len(sums)):
            sums[idx] += sums[idx-1]
        for idx, item in enumerate(sums):
            if item == s:
                res = min(res, idx + 1)
            if item > s:
                res = min(res, idx - self.bisearch(0, idx + 1, item - s, sums))
        if res != 1 << 64:
            return res
        else:
            return 0

if __name__ == "__main__":
    a=Solution()
    print a.minSubArrayLen(11, [1, 2, 3, 4, 5])




class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if len(nums)==0:
            return 0
        left,right,tmpsum,res=0,0,nums[0],1<<64
        while True:
            if tmpsum<s:
                right+=1
                if right<len(nums):
                    tmpsum+=nums[right]
                else:
                    break
            elif tmpsum>=s:
                res=min(res,right-left+1)
                if left<len(nums):
                    tmpsum-=nums[left]
                else:
                    break 
                left+=1
        return res if res!=1<<64 else 0

class Solution:
    def minSubArrayLen(self, s, nums):
        total=left=0
        res=1<<64   
        for idx,item in enumerate(nums):
            total+=item
            while total>=s:
                res=min(res,idx-left+1)
                total-=nums[left]
                left+=1
        return res if res!=1<<64 else 0
