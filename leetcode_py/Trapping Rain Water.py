# only need to find the maximum
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        if not height:
            return 0
        maxs, maxs_idx = -1, -1
        for idx, item in enumerate(height):
            if item > maxs:
                maxs_idx = idx
                maxs = item
        left, right = height[0], height[-1]
        res = 0
        for i in range(1, maxs_idx):
            if height[i] > left:
                left = height[i]
            else:
                res += left - height[i]

        for i in range(len(height)-1, maxs_idx, -1):
            if height[i] > right:
                right = height[i]
            else:
                res += right - height[i]
        return res

#
# class Solution:
#     # @param {integer[]} height
#     # @return {integer}
#     def trap(self, height):
#         rightmax=[]
#         tmpmax=-1<<64
#         for i in range(len(height)-1,-1,-1):
#             tmpmax=max(tmpmax,height[i])
#             rightmax.insert(0,tmpmax)
#         res=0
#         leftmax=-1<<64
#         for i in range(len(height)):
#             if height[i]>=leftmax:
#                 leftmax=max( height[i],leftmax)
#             else:
#                 res+=min(leftmax,rightmax[i])-height[i]
#         return res
#
#
#
#
#
#
# class Solution:
#     def cal(self,left,right,A):
#         res=0
#         item=min(A[left],A[right])
#         for i in range(left+1,right):
#             res+=item-A[i]
#         return res
#     # @param A, a list of integers
#     # @return an integer
#     def trap(self, A):
#         if len(A)<3:
#             return 0
#         ref=[i for i in A]
#         maxs=-2<<64
#         for i in xrange(len(A)-1,-1,-1):
#             if maxs<A[i]:
#                 maxs=A[i]
#             else:
#                 ref[i]=maxs
#
#         res=0
#         begin=True
#         for idx,item in enumerate(A):
#             if begin:
#                 leftidx=idx
#                 begin=False
#
#             if item>=ref[idx] or item>=A[leftidx]:
#                 res+=self.cal(leftidx,idx,A)
#                 leftidx=idx
#         return res

if __name__=="__main__":
    a=Solution()
    print a.trap( [3,1,1,1,1,1,3])  
    print a.trap( [0,1,0,2,1,0,1,3,2,1,2,1])                   
