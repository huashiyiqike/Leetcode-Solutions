import math
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n<3:
            return 0
        flag=[0,0]+ [1] * (n-2)
        
        end=int(math.sqrt(n))+1
        for i in range(2,end):
            if flag[i]==1:
                j=i
                while j+i<n:
                    j+=i
                    flag[j]=0
        return sum(flag)
  
    
if __name__=="__main__":
    a=Solution()
    print a.countPrimes(2)     
    print a.countPrimes(5)           