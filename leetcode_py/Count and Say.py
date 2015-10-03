class Solution:
    def nexts(self, strs):
        left, right = 0, 0
        res = ''
        while left < len(strs):
            while right < len(strs) and strs[right] == strs[left]:
                right += 1
            res += "{0}{1}".format(right - left, strs[left])  # str(right-left)+strs[left]
            left = right
        return res

    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        strs = '1'
        for i in range(n - 1):
            strs = self.nexts(strs)
        return strs


class Solution:
    def next(self, strs):
        res = ''
        first = False
        for idx, item in enumerate(strs):
            if not first:
                first = True
                target = item
                count = 1

                # counting same
            if idx + 1 < len(strs) and strs[idx + 1] == item:
                count += 1
            # start new
            else:
                res += str(count)
                res += str(target)
                first = False
        return res

    # @return a string
    def countAndSay(self, n):
        nstr = str(1)
        for i in range(n - 1):
            nstr = self.next(nstr)
        return nstr


if __name__ == "__main__":
    a = Solution()
    print a.countAndSay(2)
