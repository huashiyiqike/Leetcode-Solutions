class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        res=[1]
        for i in range(1,rowIndex+1):
            res=[1]+[res[f]+res[f+1] for f in range(i-1)]+[1]
        return res
#         if rowIndex==0:
#             return[1]
#         old=[1]
#         new=[0 for i in range(rowIndex+1)]
#         for i in range(1,rowIndex+1):
#             for j in range(i+1):
#                 if j==0 or j==i:
#                     new[j]=1
#                 else:
#                     new[j]=old[j-1]+old[j]
#             old=[i for i in new]
#         return new
    
if __name__=="__main__":
    a=Solution()
    print a.getRow(3)