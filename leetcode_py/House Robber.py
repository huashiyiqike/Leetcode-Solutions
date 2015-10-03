class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        dp=[0 for i in range(len(nums)+2)]
        for idx,item in enumerate(nums):
            dp[idx+2]=max(dp[idx]+item, dp[idx+1])
        return dp[-1]
#TLE
# class Solution:
#     def f(self,start,nums):
#        # print start
#         if start==len(nums)-1:
#             return nums[start]
#         elif start==len(nums)-2:
#             return max(nums[start-2],nums[start-1])
#         else:
#             return max(nums[start]+self.f(start+2,nums),self.f(start+1,nums))
#         
#     # @param {integer[]} nums
#     # @return {integer}
#     def rob(self, nums):
#         if len(nums)==0:
#             return 0
# 
#         else:
#             return self.f(0,nums)
        
if __name__=="__main__":
    a=Solution()
    print a.rob([183,219,57,193,94,233,202,154,65,240,97])#,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211])