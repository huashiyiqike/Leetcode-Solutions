class Solution:
    # @param s, a string
    # @return a list of lists of string
    def minCut(self, s):
        dp = [[False]*len(s) for i in range(len(s))]
        mincut = [i for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if i == j:
                    dp[i][j] = True
                elif j+1 == i and s[j] == s[i]:
                    dp[i][j] = True
                elif dp[i-1][j+1] and s[j] == s[i]:
                    dp[i][j] = True
                if dp[i][j]:
                    if j > 0:
                        mincut[i] = min(mincut[i], mincut[j-1]+1)
                    else:
                        mincut[i] = 0
        return mincut[-1]

class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        dpcut=[i for i in range(len(s))]
        dpmat=[[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            dpmat[i][i]=True
            if i+1<len(s) and s[i]==s[i+1]:
                dpmat[i][i+1]=True

        for i in range(len(s)-3,-1,-1):
            for j in range(i+2,len(s)):
                if s[i]==s[j] and dpmat[i+1][j-1]:
                    dpmat[i][j]=True
                   
        for i in range(len(s)):
            for j in range(i,len(s)):
                if dpmat[i][j]:
                    if i>0:
                        dpcut[j]=min(dpcut[j],1+dpcut[i-1])
                    else:
                        dpcut[j]=min(dpcut[j],0)

        return dpcut[-1]

if __name__=="__main__":
    a=Solution()
    print a.minCut('aab')
    print a.minCut('bb')