class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
      map = {}
      for idx, item in enumerate(num, start=1):
        if item not in map:
          map[target-item] = idx
        else:
          return [ map[item],idx]

# class Solution:
#     # @return a tuple, (index1, index2)
#     def twoSum(self, num, target):
#         lists=sorted(num)
#         first=0
#         last=len(lists)-1
#         while first<last:
#             if lists[first]+lists[last]<target:
#                 first+=1
#             elif lists[first]+lists[last]>target:
#                 last-=1
#             elif lists[first]+lists[last]==target:
#                 break
#         for index,item in enumerate(num):
#             if item==lists[first]:
#                 index1=index+1
#                 break
#             
#         for index,item in enumerate(num):
#             if item==lists[last] and index1!=index+1:
#                 index2=index+1
#                 break
#             
#         if index2<index1:
#             return (index2,index1)
#         else:
#             return (index1,index2)
#             
#             
# class Solution:
#     # @return a tuple, (index1, index2)
#     def twoSum(self, num, target):
#         d={}
#         for index,item in enumerate(num,start=1):
#             if item in d:
#                 return (d[item],index)
#             d[target-item]=index    
#             
