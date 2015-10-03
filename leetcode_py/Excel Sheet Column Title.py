class Solution:
    # @return a string
    def convertToTitle(self, num):
        dicts = [0] * 26
        for i in range(1, 26):
            dicts[i] = chr(ord('A') + i - 1)
        dicts[0] = 'Z'
        res = ''
        while num > 0:
            res = dicts[num % 26] + res
            if num % 26 == 0:
                num -= 26
            num /= 26
        return res


class Solution:
    # @return a string
    def convertToTitle(self, num):
        dicts = {}
        res = ''
        for i in range(65, 65 + 26):
            dicts[i - 64] = chr(i)  # 0-25
        dicts[0] = 'Z'

        while num > 0:
            res = dicts[num % 26] + res
            if num % 26 == 0:
                num -= 1
            num /= 26
        return res


if __name__ == "__main__":
    a = Solution()
    print a.convertToTitle(26 * 27)
    for i in xrange(1, 55):
        print a.convertToTitle(i)
