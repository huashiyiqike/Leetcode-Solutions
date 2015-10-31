class Solution:
    def find(self, a, b):
        for i in range(len(b)):
            if a[i] != b[i]:
                return False
        return True

    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        for idx in range(len(haystack) - len(needle) + 1):
            if haystack[idx] == needle[0]:
                if self.find(haystack[idx:], needle):
                    return idx
        return -1
