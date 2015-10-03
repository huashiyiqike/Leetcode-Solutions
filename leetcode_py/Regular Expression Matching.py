class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not s and not p:
            return True
        elif not p:
            return False
        if s and s[0] == p[0]:
            if len(p)>1 and p[1] == '*':
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s[1:], p[1:])
        if s and p[0] == '.':
            if len(p)>1 and p[1] == '*':
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s[1:], p[1:])
        if len(p)>1 and p[1] == '*':
            return self.isMatch(s, p[2:])
        return False

#  TLE
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not s and not p:
            return True
        elif not p:
            return False

        if len(p)>1 and p[1] == '*':
            if s and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:]) #self.isMatch(s[1:], p[2:])
            else:
                return self.isMatch(s, p[2:])

        elif s and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])

        else:
            return False


class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not s and not p:
            return True

        if not p and s:
            return False

        if p[-1] == '*':
            rep = p[-2]
            if s and (s[-1] == rep or rep == '.'):
                return self.isMatch(s[:-1], p) or self.isMatch(s, p[:-2])
            else:
                return self.isMatch(s, p[:-2])
        else:
            if s and (p[-1] == s[-1] or p[-1] == '.'):
                return self.isMatch(s[:-1], p[:-1])
            else:
                return False

if __name__=="__main__":
    a=Solution()
    #print a.isMatch("caaaaaaaaaaaaaaa", "a*a*a*a*a*a*a*a*a*a*a*")
    print a.isMatch("abcdede", "ab.*de")
    print a.isMatch("aaa", ".*")
    print a.isMatch("aaa", "ab*a")
    print a.isMatch("ab", ".*..")
    print a.isMatch("a", "ab*")
    print a.isMatch("aaca", "ab*a*c*a")
    print a.isMatch("aaa", "ab*a*c*a")
    print a.isMatch("aab", "c*a*b")
    print a.isMatch("aa", '.*')
    print a.isMatch("aac", 'a.c')
    print a.isMatch('aac', 'a*c')
    print a.isMatch('aaaaaac', 'a*c')
    print a.isMatch('aaa', 'a*')
    print a.isMatch('aaaa', 'a*c')
    print a.isMatch('aaaacaaa', 'a*ca*a')
    print ''


class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        dp = [[False]*(len(p)+1) for i in range(len(s)+1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            if i >=1 and p[i-1] == '*' and dp[0][i-2]:
                dp[0][i] = True
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    if dp[i-1][j-1]:
                        dp[i][j] = True
                elif p[j-1] == '*':
                    # one
                    if dp[i][j-1]:
                        dp[i][j] = True
                     # zero
                    elif j > 2 and dp[i][j-2]:
                        dp[i][j] = True
                    elif j > 1:
                        # many
                        if dp[i-1][j-1] and (p[j-2] == s[i-1] or p[j-2] == '.'):
                            dp[i][j] = True
                        # any
                        if dp[i-1][j] and p[j-2] == '.':
                            dp[i][j] = True

        return dp[-1][-1]

if __name__=="__main__":
    a=Solution()
    print a.isMatch("abcdede", "ab.*de")
    print a.isMatch("aaa", ".*")
    print a.isMatch("aaa", "ab*a")
    print a.isMatch("ab", ".*..")
    print a.isMatch("a", "ab*")
    print a.isMatch("aaca", "ab*a*c*a")
    print a.isMatch("aaa", "ab*a*c*a")
    print a.isMatch("aab", "c*a*b")
    print a.isMatch("aa", '.*')
    print a.isMatch("aac", 'a.c')
    print a.isMatch('aac', 'a*c')
    print a.isMatch('aaaaaac', 'a*c')
    print a.isMatch('aaa', 'a*')
    print a.isMatch('aaaa', 'a*c')
    print a.isMatch('aaaacaaa', 'a*ca*a')
    print ''

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        dp = [ [False for j in range(len(p) + 1) ] for i in range(len(s) + 1) ]
        dp[0][0] = True
        for i in range(1, len(dp[0])):
            if i > 1 and p[i - 1] == '*' and dp[0][i - 2]:
                dp[0][i] = True
                #  print dp

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if  s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif   p[j - 1] == '*':
                    dp[i][j] =  dp[i][j - 1] or (j > 1 and dp[i][j - 2]) \
                    or ((dp[i - 1][j - 1 ] or  dp[i - 1][j ])  and \
                    (j > 1 and s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        #print dp
        return dp[len(s) ][len(p) ]

    
if __name__=="__main__":
    a=Solution()
    print a.isMatch("abcdede", "ab.*de")
    print a.isMatch("aaa", ".*")
    print a.isMatch("aaa", "ab*a")
    print a.isMatch("ab", ".*..")
    print a.isMatch("a", "ab*")
    print a.isMatch("aaca", "ab*a*c*a")
    print a.isMatch("aaa", "ab*a*c*a")
    print a.isMatch("aab", "c*a*b")
    print a.isMatch("aa", '.*')
    print a.isMatch("aac", 'a.c')
    print a.isMatch('aac', 'a*c')
    print a.isMatch('aaaaaac', 'a*c')
    print a.isMatch('aaa', 'a*')
    print a.isMatch('aaaa', 'a*c')
    print a.isMatch('aaaacaaa', 'a*ca*a')
    print ''
    