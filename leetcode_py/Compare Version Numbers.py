class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        a = map(int, version1.split('.'))
        b = map(int, version2.split('.'))
        a += [0] * (max(len(b), len(a)) - len(a))
        b += [0] * (max(len(b), len(a)) - len(b))
        return cmp(a, b)

# @param version1, a string
# @param version2, a string
# @return an integer
def compareVersion(self, version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    i = 0
    while i < min(len(v1), len(v2)):
        if int(v1[i]) > int(v2[i]):
            return 1
        elif int(v1[i]) < int(v2[i]):
            return -1
        i += 1

    if len(v1) > len(v2) and sum([int(item) for item in v1[i:]]) != 0:
        return 1
    elif len(v1) < len(v2) and sum([int(item) for item in v2[i:]]) != 0:
        return -1
    else:
        return 0


if __name__ == "__main__":
    a = Solution()
    print a.compareVersion("01", "1")
    print a.compareVersion("1.0", "1")
