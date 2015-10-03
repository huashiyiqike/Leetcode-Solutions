class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        res = []
        if not nums:
            return res
        start = end = None
        for i in nums:
            if start == None:
                start = end = i
            elif i == end+1:
                end += 1
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append("{}->{}".format(start, end))
                start = end = i
        if start != None:
            if start == end:
                res.append(str(start))
            else:
                res.append("{}->{}".format(start, end))
        return res

if __name__ == "__main__":
    a = Solution()
    print a.summaryRanges([0])
    print a.summaryRanges([0, 1])
    print a.summaryRanges([1, 3])

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        start = -1 << 64
        end = - 1 << 64
        idx = 0
        res = []
        while idx < len(nums):
            if start == -1 << 64:
                start = end = nums[idx]

            elif nums[idx] == end+1:
                end += 1
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start)+'->'+str(end))
                if idx == len(nums):
                    start = - 1 << 64
                else:
                    start = end = nums[idx]

            idx += 1

        if start != -1 << 64:
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start)+'->'+str(end))

        return res


if __name__ == "__main__":
    a = Solution()
    print a.summaryRanges([1, 3])


class Solution:
    def summaryRanges(self, nums):
            if not nums:
                return []
        res = []
        i = 0
        start = 0
        while i < len(nums)-1:
            if nums[i]+1 != nums[i+1]:
                res.append(self.printRange(nums[start], nums[i]))
                start = i+1
            i += 1
        res.append(self.printRange(nums[start], nums[i]))
        return res

    def printRange(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + "->" + str(r)