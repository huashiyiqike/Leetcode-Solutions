class Solution:
    def f(self, digits, i, path, res):
        if i == len(digits):
            res.append(path)
            return

        for j in self.maps[ord(digits[i]) - ord('0')]:
            # print path
            self.f(digits, i + 1, path + j, res)

    # @param digits, a string
    # @return a string[]
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        self.maps = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'qprs', 'tuv', 'wxyz']
        res = []
        self.f(digits, 0, "", res)
        return res


if __name__ == "__main__":
    a = Solution()
    print a.letterCombinations("22")
