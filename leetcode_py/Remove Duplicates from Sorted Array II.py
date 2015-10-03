class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums)<1:
            return 0
        lens=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[lens-1]:
                nums[lens]=nums[i]
                lens+=1
            elif lens==1 or (lens>1 and nums[lens-2]!=nums[lens-1]):
                nums[lens]=nums[i]
                lens+=1
        return lens




class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        pre=0
        cur=0
        while pre<len(A):
            print cur,pre
            if pre+1<len(A) and A[pre+1]==A[pre]:
                i=2
                while pre+i<len(A) and A[pre+i]==A[pre]:
                    i+=1
                A[cur]=A[pre]
                A[cur+1]=A[pre]
                
                pre+=i
                cur+=2
            else:
                A[cur]=A[pre]
                
                cur+=1
                pre+=1
        return cur
        
if __name__=="__main__":
    a=Solution()
    print a.removeDuplicates([1,1,1])