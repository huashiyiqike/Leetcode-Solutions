class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s:
            return 0
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if i < len(s) - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]


class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0

        res = [0 for i in s]
        res[0] = 1
        for i in range(1, len(s)):
            if s[i] == '0' and (s[i - 1] == '0' or s[i - 1] > '2'):
                return 0
            if s[i] == '0':
                if i > 1:
                    res[i] = res[i - 2]
                else:
                    res[i] = res[i - 1]
            else:
                if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] < '7'):
                    #                     if i<len(s)-1 and s[i+1]=='0':
                    #                         res[i]=res[i-1]
                    if i == 1:
                        res[i] = res[i - 1] + 1
                    else:
                        res[i] = res[i - 1] + res[i - 2]
                else:
                    res[i] = res[i - 1]

        return res[-1]
