# TLE
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if len(s) < len(''.join(p.split('*'))):
            return False
        if not s and not p:
            return True
        elif not p:
            return False
        if p[0] == '*':
            # while len(p) > 0 and p[1] == '*':
            #     p = p[1:]
            # if not s and len(p) > 0 and p[1] != '*':
            #     return False
            return self.isMatch(s[1:], p[1:]) or self.isMatch(s[1:], p)
        elif s and (s[0] == p[0] or p[0] == '?'):
            return self.isMatch(s[1:], p[1:])
        else:
            return False


class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if len(s) < len(''.join(p.split('*'))):
            return False
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if dp[0][i - 1] and p[i - 1] == '*':
                dp[0][i] = True
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if (p[j - 1] == '?' or s[i - 1] == p[j - 1]) and dp[i - 1][j - 1]:
                    dp[i][j] = True
                elif p[j - 1] == '*' and (dp[i - 1][j - 1] or dp[i][j - 1] or dp[i - 1][j]):
                    dp[i][j] = True
        return dp[-1][-1]


class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if len(s) < len(''.join(p.split('*'))):
            return False
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(dp[0])):
            if p[i - 1] == '*' and dp[0][i - 1]:
                dp[0][i] = True

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j - 1] or dp[i - 1][j]
                    #    print dp
        return dp[len(s)][len(p)]


if __name__ == '__main__':
    a = Solution()
    if len(sys.argv) == 1:
        print a.isMatch('abefcdgiescdfimde', 'ab*cd?i*de')

        # ("aabbbbaababbabababaabbbbabbabbaabbbabbbabaabbaaaababababbababbabbbbabaaabaaabaabbaaaabbbbabaaabbbbbabbbaabbbbbabaabababaaabaaababaababbaaabaabbabaababbabababaaababbabbabaabbbbabbbbabaabbaababaaabababbab",
    #         "a*b*a*b*aaaa*abaaa**b*a***b*a*bb****ba*ba*b******a********a**baba*ab***a***bbba*b**a*b*ba*a*aaaa*ab**")
    else:
        print a.isMatch(sys.argv[1], sys.argv[2])
