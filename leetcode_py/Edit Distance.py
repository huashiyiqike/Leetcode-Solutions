class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        dp = [[2 ** 64] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word2) + 1):
            dp[0][i] = i
        for i in range(len(word1) + 1):
            dp[i][0] = i

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i][j], dp[i + 1][j])
        return dp[-1][-1]


class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if len(word2) == 0:
            if len(word1) == 0:
                return 0
            else:
                return len(word1)

        m = [[0 for j in range(1 + len(word2))] for i in range(1 + len(word1))]

        for j in range(0, len(word1) + 1):
            m[j][0] = j
        for i in range(0, len(word2) + 1):
            m[0][i] = i

        for idx in range(1, len(word1) + 1):
            for idy in range(1, len(word2) + 1):
                if word1[idx - 1] == word2[idy - 1]:
                    m[idx][idy] = m[idx - 1][idy - 1]
                else:
                    m[idx][idy] = 1 + min(m[idx - 1][idy], m[idx][idy - 1], m[idx - 1][idy - 1])

        return m[-1][-1]


class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        dp = [[0] * len(word2) for i in range(len(word1))]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if i == 0 and j == 0:
                    dp[i][j] = 0 if word1[i] == word2[j] else 1
                elif i == 0:
                    dp[i][j] = 1 + dp[i][j - 1] if word1[i] != word2[j] else dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = 1 + dp[i - 1][j] if word1[i] != word2[j] else dp[i - 1][j]
                elif word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if len(word2) == 0:
            if len(word1) == 0:
                return 0
            else:
                return len(word1)

        m = [[0 for j in range(1 + len(word2))] for i in range(1 + len(word1))]

        for j in range(0, len(word1) + 1):
            m[j][0] = j
        for i in range(0, len(word2) + 1):
            m[0][i] = i

        for idx in range(1, len(word1) + 1):
            for idy in range(1, len(word2) + 1):
                if word1[idx - 1] == word2[idy - 1]:
                    m[idx][idy] = m[idx - 1][idy - 1]
                else:
                    m[idx][idy] = 1 + min(m[idx - 1][idy], m[idx][idy - 1], m[idx - 1][idy - 1])

        return m[-1][-1]


if __name__ == "__main__":
    a = Solution()
    print a.minDistance("dinitrophenylhydrazine", "dimethylhydrazine")
