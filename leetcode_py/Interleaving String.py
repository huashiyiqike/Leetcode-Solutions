class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        elif not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1)):
            for j in range(len(s2)):
                if dp[i][j]:
                    if s1[i] == s3[i + j]:
                        dp[i + 1][j] = True
                    if s2[j] == s3[i + j]:
                        dp[i][j + 1] = True
                if dp[i + 1][j]:
                    if s2[j] == s3[i + j + 1]:
                        dp[i + 1][j + 1] = True
                if dp[i][j + 1]:
                    if s1[i] == s3[i + j + 1]:
                        dp[i + 1][j + 1] = True

        return dp[-1][-1]


class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): return False
        dp = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        for i in range(0, len(s1) + 1):
            for j in range(0, len(s2) + 1):  # k is determined
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:  # "aa", "ab", "abaa" length of s1 is 0
                    dp[i][j] = s2[:j] == s3[:j]
                elif j == 0:  # length of s2 is 0
                    dp[i][j] = s1[:i] == s3[:i]
                else:
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]


class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[0][0] = True
                elif i == 0:
                    dp[i][j] = s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]
                else:
                    dp[i][j] = (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]) or \
                               (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j])
        return dp[-1][-1]


if __name__ == '__main__':
    a = Solution()
    print a.isInterleave("ab", "bc", "bcab")
    print a.isInterleave("db", "b", "cbb")


class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 == s3 and len(s2) == 0:
            return True
        if s2 == s3 and len(s1) == 0:
            return True
        mat = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        mat[0][0] = 1
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if mat[i - 1][j - 1] == 1:
                    if s1[i - 1] == s3[i + j - 2]:
                        mat[i][j - 1] = 1
                    if s2[j - 1] == s3[i + j - 2]:
                        mat[i - 1][j] = 1
                if mat[i - 1][j] == 1 and s1[i - 1] == s3[i + j - 1]:
                    mat[i][j] = 1
                if mat[i][j - 1] == 1 and s2[j - 1] == s3[i + j - 1]:
                    mat[i][j] = 1

        return mat[len(s1)][len(s2)] == 1


if __name__ == '__main__':
    import sys

    a = Solution()
    if len(sys.argv) == 1:
        print a.isInterleave('aabd', 'abdc', 'aabdabcd')
        print a.isInterleave('a', '', 'a')
    else:
        print a.isInterleave(sys.argv[1], sys.argv[2], sys.argv[3])
