import math

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        res = ''
        k -= 1
        nums = [str(i) for i in range(1, n+1)]
        while n > 0:
            tmp = math.factorial(n-1)
            res += nums[k/tmp]
            del nums[k/tmp]
            k %= tmp
            n -= 1
        return res



# class Solution:
#     def f(self,n,k):
#         if n==1 :
#             return [0]
#         else:
#             count=1
#             for i in range(1,n):
#                 count*=i
#             begin=(k-1)/count
#             plus=k%count
#         return [begin]+self.f(n-1,plus)
#
#     # @return a string
#     def getPermutation(self, n, k):
#         res=self.f(n,k)
#         print res
#         lists=range(1,n+1)
#         strs=''
#         for i in range(n):
#             strs+=str(lists[res[i]])
#             lists.pop(res[i])
#         return strs

if __name__=="__main__":
    a=Solution()
    print a.getPermutation(3, 1),"123"
    print a.getPermutation(2,2)
    print a.getPermutation(3,2)
#https://leetcode.com/discuss/16064/an-iterative-solution-for-reference

#TLE
# class Solution:
#     def f(self,lists):
#         if lists==None:
#             return None
#         tmpres=[]
#             
#         for idx,item in enumerate(lists):
#             tmp=[i for i in lists]
#             tmp.pop(idx)
#             res=self.f(tmp)
#             if len(res)>0:
#                 for i in res:
#                     tmpres.append(str(item)+i)
#             else:
#                 tmpres.append(str(item))
#         return tmpres
#             
#     # @return a string
#     def getPermutation(self, n, k):
#         if n==1:
#             return '1'
#         count=1
#         begin=0
#         plus=0
#         for i in range(1,n):
#             count*=i
#         begin+=k/count
#         plus=k%count
#         
#         tmp=[i for i in range(1,n+1)]
#         if begin>0:
#             tmp.pop(begin-1)
#         
#         tmp=self.f(tmp)
#         if begin>0:
#             return str(begin)+tmp[plus-1]
#         else:
#             return tmp[plus-1]
# TLE
# # class Solution:
# #     def f(self,lists):
# #         if lists==None:
# #             return None
# #         tmpres=[]
# #             
# #         for idx,item in enumerate(lists):
# #             tmp=[i for i in lists]
# #             tmp.pop(idx)
# #             res=self.f(tmp)
# #             if len(res)>0:
# #                 for i in res:
# #                     tmpres.append(str(item)+i)
# #             else:
# #                 tmpres.append(str(item))
# #         return tmpres
# #             
# #     # @return a string
# #     def getPermutation(self, n, k):
# #        tmp=self.f(range(1,n+1))
# #        return tmp[k-1]
# #         
