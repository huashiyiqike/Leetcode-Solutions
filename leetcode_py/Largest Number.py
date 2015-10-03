class Solution:
    def cmps(self, a, b):
        if a + b < b + a:
            return 1
        elif a + b == b + a:
            return 0
        else:
            return -1

    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = map(lambda x: str(x), nums)
        nums.sort(cmp=self.cmps)
        res = ''.join(nums)  # sorted(nums,cmp=self.cmps))
        if res[0] == '0' and len(res) > 0:
            return '0'
        return res


class Solution:
    def f(self, a, b):
        #  print a,b
        p1 = 0
        p2 = 0
        while p1 < len(a) and p2 < len(b):
            if a[p1] < b[p2]:
                return 1
            elif a[p1] > b[p2]:
                return -1
            p1 += 1
            p2 += 1

        if p1 == len(a) and p2 != len(b):
            return self.f(a, b[p2:])

        elif p2 == len(b) and p1 != len(a):
            return self.f(a[p1:], b)
        else:
            return 0

    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        strs = [str(i) for i in num]
        strs.sort(cmp=lambda x, y: self.f(x, y))
        for i in range(1, len(strs)):
            strs[0] += strs[i]
        while strs[0][0] == '0' and len(strs[0]) > 1:
            strs[0] = strs[0][1:]
        return strs[0]


if __name__ == "__main__":
    a = Solution()
    print a.largestNumber([12, 128])
    print a.largestNumber([1, 2, 4, 8, 16, 32, 64, 128, 256, 512])
    print a.largestNumber([2, 256])
    print a.largestNumber([824, 8247])
    print a.largestNumber([12, 121])
