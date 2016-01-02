class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        longest = strs[0]
        for str in strs[1:]:
            i = 0
            while i < len(str) and i < len(longest) and str[i] == longest[i]:
                i += 1
            longest = longest[:i]
        return longest


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        count = 0
        mins = 2 << 64
        for i in strs:
            mins = min(mins, len(i))
            # print mins

        res = 0
        r = True
        for i in range(mins):

            tmp = strs[0][i]
            for j in strs[1:]:
                if tmp != j[i]:
                    r = False
                    break

            if not r:
                break
            res = i + 1
        return strs[0][0:res] if res >= 0 else ""


if __name__ == "__main__":
    a = Solution()

    print a.longestCommonPrefix(["c", "a", "a"])
    print a.longestCommonPrefix(["a", "ab", "ab "])
