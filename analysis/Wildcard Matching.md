<backquote><pre>
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
</backquote></pre>
Similar with Regular Expression Matching, but time limit is more demanding, recursive call will get TLE. We can only use Dynamic programming here. Notice that in initialization we should consider the case that p start with '*'.

<backquote><pre> 
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

</backquote></pre>