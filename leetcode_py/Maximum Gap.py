import sys


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        bucketmin = [sys.maxint] * (len(nums) - 1)
        bucketmax = [-sys.maxint] * (len(nums) - 1)
        start = min(nums)
        dis = (max(nums) - start) / (len(nums) - 1) + 1

        for i in nums:
            idx = (i - start) / dis
            bucketmin[idx] = min(i, bucketmin[idx])
            bucketmax[idx] = max(i, bucketmax[idx])
        res = None
        lastmaxs = bucketmax[0]
        for i in range(len(nums) - 1):
            res = max(res, bucketmax[i] - bucketmin[i])  # within bucket
            if bucketmin[i] != sys.maxint:  # or buckmax[i] != -sys.maxint
                res = max(res, bucketmin[i] - lastmaxs)  # between bucket
                lastmaxs = bucketmax[i]

        return res


if __name__ == "__main__":
    a = Solution()
    print a.maximumGap([100, 3, 2, 1])
    print a.maximumGap([1, 100000])


class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        maxs = -1 << 64
        mins = 1 << 64
        for i in num:
            if i > maxs:
                maxs = i
            if i < mins:
                mins = i
        if maxs == mins:
            return 0

        duration = max(1, int(0.5 + 1.0 * (maxs - mins) / (len(num) - 1)))  # (maxs-mins)/(len(num)-1)+1
        numb = (maxs - mins) / duration + 1
        bucket = [None for i in range(numb)]
        #  print bucket
        for i in num:
            idx = (i - mins) / duration
            # print (i-mins)/duration,duration
            if bucket[idx] == None:
                bucket[idx] = [i, i]

            else:
                if i < bucket[idx][0]:
                    bucket[idx][0] = i
                if i > bucket[idx][1]:
                    bucket[idx][1] = i
        res = 0
        # print bucket
        for i in range(0, numb - 1):
            if bucket[i] != None:
                for j in range(i + 1, numb):
                    if bucket[j] != None:
                        res = max(res, bucket[j][0] - bucket[i][1])
                        break
        return res


if __name__ == "__main__":
    a = Solution()
    print a.maximumGap([100, 3, 2, 1])
    print a.maximumGap([1, 100000])
