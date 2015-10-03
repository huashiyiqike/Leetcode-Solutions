class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        cur, one, two = 0, -1, len(nums)
        while cur < two:
            if nums[cur] == 0:
                one += 1
                nums[one], nums[cur] = nums[cur], nums[one]
                if one >= cur:
                    cur = one + 1
            elif nums[cur] == 2:
                two -= 1
                nums[two], nums[cur] = nums[cur], nums[two]
            else:
                cur += 1

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        if len(nums)==0:
            return
        start,end=0,len(nums)-1
        while  nums[start]==0:
            start+=1
            if start>=len(nums):
                return
        while  nums[end]==2:
            end-=1
            if end<0:
                return

        i=start
        while i<=end:
            if nums[i]==0:
                nums[i],nums[start]=nums[start],nums[i]
                start+=1
                if start>i:
                    i+=1
            elif nums[i]==2:
                nums[i],nums[end]=nums[end],nums[i]
                end-=1
            else:
                i+=1
        return

            
if __name__=='__main__':
    a=Solution()

    print a.sortColors([1,0])
    print a.sortColors([0,1,2,0,2,1,0,2])
    print a.sortColors([2])
    print a.sortColors([2,1])
    print a.sortColors([1,2,0])
    print a.sortColors([2,0,0])
    print a.sortColors([])

        
#
# class Solution:
#     def sortColors(self, A):
#         i, last_zero, first_two = 0, -1, len(A)
#         while i < first_two:
#             if A[i] == 0:
#                 last_zero += 1
#                 A[last_zero], A[i] = A[i], A[last_zero]
#             if A[i] == 2:
#                 first_two -= 1
#                 A[first_two], A[i] = A[i], A[first_two]
#                 i -= 1
#             i += 1
