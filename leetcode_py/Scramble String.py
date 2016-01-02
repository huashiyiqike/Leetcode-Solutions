# Memoization DP
# https://leetcode.com/discuss/22463/accepted-python-solution-whats-time-complexity-this-solution
# 482ms
class Solution:
    def __init__(self):
        self.cache = {}

    def isScramble(self, s1, s2):
        if sorted(s1) != sorted(s2):
            return False
        if (s1, s2) in self.cache:
            return self.cache[(s1, s2)]

        if len(s1) == 1:
            self.cache[(s1, s2)] = (s1 == s2)
            return self.cache[(s1, s2)]

        length = len(s2)
        for i in range(1, length):  # split point 1~len(s2)-1
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) \
                    or (self.isScramble(s1[length - i:], s2[:i]) and self.isScramble(s1[:length - i], s2[i:])):
                self.cache[(s1, s2)] = True
                return True
        self.cache[(s1, s2)] = False
        return False


# set not good, need to evaluate twice if not in set
class Solution:
    def __init__(self):
        self.cache = set()

    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        if sorted(s1) != sorted(s2):
            return False
        if (s1, s2) in self.cache:
            return True
        if len(s1) == 1:
            if s1 == s2:
                self.cache.add((s1, s2))
                return True
            else:
                return False

        length = len(s2)
        for i in range(1, length):
            if (self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i], s2[:i])) or \
                    (self.isScramble(s1[length - i:], s2[:i]) and self.isScramble(s1[:length - i], s2[i:])):
                self.cache.add((s1, s2))
                return True
        return False


#
#
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        else:
            res = False
            for i in range(1, len(s1)):
                res |= (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) \
                       or (self.isScramble(s1[i:], s2[:len(s1) - i]) and self.isScramble(s1[:i], s2[len(s1) - i:]))
                if res:
                    return True
            return res


#TLE


class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        if sorted(s1) != sorted(s2):
            return False

        dp = [[[False for i in range(len(s1) + 1)] for j in range(len(s1))] for k in range(len(s1))]

        for i in range(len(s1)):
            for j in range(len(s1)):
                dp[i][j][1] = (s1[i] == s2[j])

        for k in range(len(s1) + 1):
            for i in range(len(s1) - 1, -1, -1):
                for j in range(len(s1) - 1, -1, -1):
                    #                     if k==0:
                    #                         pass#dp[i][j][k]=True
                    #                     elif k==1:
                    #                         dp[i][j][k]=(s1[i]==s2[j])
                    #                     elif k==2:
                    #                         if i+2<=len(s1) and j+2<=len(s2):
                    #                             dp[i][j][k]=(  s1[i:(i+2)]==s2[j:(j+2)] or s1[i:(i+2)]==s2[j:(j+2)][::-1]  )
                    #                             print s1[i:(i+2)],s2[j:(j+2)]
                    #                             print s1[i:(i+2)],s2[j:(j+2)][::-1]
                    # else:
                    for m in range(1, k):
                        if i + m < len(s1) and j + m < len(s1) and j + k - m < len(s1):
                            dp[i][j][k] |= (dp[i][j][m] and dp[i + m][j + m][k - m]) or (
                            dp[i + m][j][k - m] and dp[i][j + k - m][m])
                            if dp[i][j][k]:
                                break
                                # print dp
        return dp[0][0][len(s1)]


if __name__ == "__main__":
    a = Solution()
    # print a.isScramble("a","a")
    print a.isScramble("abcdefghijklmnopq", "efghijklmnopqcadb")
    print a.isScramble("oyifgtdmeyslstaojpppxvxiavcije", "oaacejivixvxpppjotslsyemdtgfiy")
    print a.isScramble("dsanujiiqwfsysnfsrwbrfhhpqicbw", "dabbciwqphhfrwrsfnsysfwqiijuns")
    print a.isScramble("ab", "ba")
    print a.isScramble("abab", "bbaa")
    print a.isScramble("abc", "cab")
    print a.isScramble("abcet", "cabet")
    print a.isScramble('great', 'rgeat')
    print a.isScramble('great', 'ergta')
    print a.isScramble('abcde', 'caebd')
