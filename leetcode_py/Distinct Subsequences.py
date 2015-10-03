class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        dp = [[0]*(len(t)+1) for i in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        #print dp
        return dp[-1][-1]
if __name__=="__main__":
    a=Solution()
    print a.numDistinct("aacaacca", "ca")
    print a.numDistinct("ccc", "c")
    print a.numDistinct('b','a')
    #     print a.numDistinct("aaaaa", "")
    print a.numDistinct("aaaaa", "aa")
    print a.numDistinct("aabbb", "abb")
    print a.numDistinct("rabbbiit", "rabbit")
    print ''


class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if len(T)==0:
            return 1
        m=[[0 for i in range(len(S)+1)] for j in range(len(T)+1)]
        m[0][0]=1
        for i in range(0,len(T)+1):
            for j in range(0,len(S)+1):
#                 if i==len(T)-1:
#                     m[i][j]=1
                if S[j-1]==T[i-1]:
                   # print S[j],T[i]
                    #m[i][j]=1
                    if i>0 and j>0:
                        m[i][j]+=m[i-1][j-1]
                if j>0:
                    m[i][j]+=m[i][j-1]
        return m[-1][-1]
    
if __name__=="__main__":
    a=Solution()
    print a.numDistinct("aacaacca", "ca")
    print a.numDistinct("ccc", "c")
    print a.numDistinct('b','a')
#     print a.numDistinct("aaaaa", "")
    print a.numDistinct("aaaaa", "aa")
    print a.numDistinct("aabbb", "abb")
    print a.numDistinct("rabbbiit", "rabbit")
