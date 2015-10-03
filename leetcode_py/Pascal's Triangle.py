class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows: return []
        tmp = [1]
        res = [[1]]
        for i in range(1, numRows):
            newres = [1]
            for i in range(len(tmp)-1):
                newres.append(tmp[i] + tmp[i+1])
            newres.append(1)
            res.append(newres)
            tmp = newres
        return res

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows==0:
            return []
        list=[[1]]
        for i in range(1,numRows):
            tmplist=[1]
            for j in range(1,i):
                tmplist.append(list[i-1][j-1]+list[i-1][j])
            tmplist.append(1)    
            list.append(tmplist)
            
        return list