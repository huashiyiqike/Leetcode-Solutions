
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        digits=[0 for i in range(63)]
        for i in A:
            for j in range(63):
                if i>>j&1:
                    print j
                    digits[j]+=1
        res=0
        for i in range(63):
            res+=(digits[i]%2)<<i
        return self.convert(res)

    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x
    
if __name__=="__main__":
    a=Solution()
    print a.singleNumber([-1])        
#         
# class Solution:
#     # @param A, a list of integer
#     # @return an integer
#     def singleNumber(self, A):
#         res=A[0]
#         for i in range(1,len(A)):
#             res^=A[i]
#         return res
#         
# class Solution:
#     # @param A, a list of integer
#     # @return an integer
#     def singleNumber(self, A):
#         list=set()
#         for i in A:
#             if i in list:
#                 list.remove(i)
#             else:
#                 list.add(i)
#         return list.pop()        