class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        col0=1
        for idx in range(len(matrix)):
            if matrix[idx][0]==0: col0=0
            for idy  in range(1,len(matrix[0])):
                if matrix[idx][idy]==0:
                    matrix[idx][0]=matrix[0][idy]=0
                    
        for i in range(len(matrix)-1,-1,-1):
            for j in range(1,len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if col0==0:
                matrix[i][0]=0
               
            
        

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        for idx,item in enumerate(matrix):
            for idy,item2 in enumerate(item):
                if item2==0:
                    for i in range(len(matrix)):
                        if matrix[i][idy]!=0:
                            matrix[i][idy]=1<<61
                    for i in range(len(matrix[0])):
                        if matrix[idx][i]!=0:
                            matrix[idx][i]=1<<61
                elif idx>0 and matrix[idx-1][idy]==0:
                    matrix[idx][idy]=1<<61
                elif idy>0 and matrix[idx][idy-1]==0:
                    matrix[idx][idy]=1<<61
        
        for idx,item in enumerate(matrix):
            for idy,item2 in enumerate(item):
                if item2==1<<61:
                    matrix[idx][idy]=0

import sys
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
                
    def setZeroes(self, matrix):

        xaxis=[]
        yaxis=[]
        for idx,item in enumerate(matrix):
            for idy,item2 in enumerate(item):
                if item2==0:
                    xaxis.append(idx)
                    yaxis.append(idy)
        for i in xaxis:
            for j,item in enumerate(matrix[i]):
                matrix[i][j]=0
   
        for i in yaxis:
            for x in range(len(matrix)):
                matrix[x][i]=0
        print matrix
                
if __name__ == '__main__':
    a = Solution()
    if len(sys.argv) == 1:	
        print a.setZeroes([[0,1]])
        
        #("aabbbbaababbabababaabbbbabbabbaabbbabbbabaabbaaaababababbababbabbbbabaaabaaabaabbaaaabbbbabaaabbbbbabbbaabbbbbabaabababaaabaaababaababbaaabaabbabaababbabababaaababbabbabaabbbbabbbbabaabbaababaaabababbab",
#         "a*b*a*b*aaaa*abaaa**b*a***b*a*bb****ba*ba*b******a********a**baba*ab***a***bbba*b**a*b*ba*a*aaaa*ab**")
    else:
        print a.isMatch(sys.argv[1], sys.argv[2])
# 
# 
# My idea is simple: store states of each row in the first of that row, and store states of each column in the first of that column. Because the state of row0 and the state of column0 would occupy the same cell, I let it be the state of row0, and use another variable "col0" for column0. In the first phase, use matrix elements to set states in a top-down way. In the second phase, use states to set matrix elements in a bottom-up way.
# 
# void setZeroes(vector<vector<int> > &matrix) {
#     int col0 = 1, rows = matrix.size(), cols = matrix[0].size();
# 
#     for (int i = 0; i < rows; i++) {
#         if (matrix[i][0] == 0) col0 = 0;
#         for (int j = 1; j < cols; j++)
#             if (matrix[i][j] == 0)
#                 matrix[i][0] = matrix[0][j] = 0;
#     }
# 
#     for (int i = rows - 1; i >= 0; i--) {
#         for (int j = cols - 1; j >= 1; j--)
#             if (matrix[i][0] == 0 || matrix[0][j] == 0)
#                 matrix[i][j] = 0;
#         if (col0 == 0) matrix[i][0] = 0;
#     }
# }