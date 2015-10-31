class maxqueue(object):
    def __init__(self):
        self.queue = []
        self.maxs = []

    def push(self, x):
        self.queue.append(x)
        while self.maxs and self.maxs[-1] < x:
            self.maxs.pop()
        self.maxs.append(x)

    def pop(self):
        if self.queue[0] == self.maxs[0]:
            self.maxs.pop(0)
        self.queue.pop(0)

    def mymax(self):
        return self.maxs[0]

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        res = []
        q = maxqueue()
        for i in range(k):
            if i < len(nums):
                q.push(nums[i])
        res.append(q.mymax())
        for i in range(k, len(nums)):
            q.pop()
            q.push(nums[i])
            res.append(q.mymax())
        return res

# TLE
import heapq
from collections import defaultdict


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        if len(nums) <= k:
            return [max(nums)]
        dict = defaultdict(int)
        queue = []
        res = []
        for i in range(k):
            dict[nums[i]] += 1
            heapq.heappush(queue, -nums[i])
            # print -heapq.nsmallest(1, queue)[0]
        res.append(-heapq.nsmallest(1, queue)[0])

        for i in range(k, len(nums)):
            dict[nums[i - k]] -= 1
            dict[nums[i]] += 1
            heapq.heappush(queue, -nums[i])
            largest = -heapq.nsmallest(1, queue)[0]
            while dict[largest] <= 0:
                largest = -heapq.heappop(queue)
            res.append(largest)

        return res


if __name__ == "__main__":
    a = Solution()
    print a.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)

# https://leetcode.com/discuss/65240/python-simple-solution
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        ans = []
        queue = []
        for i, v in enumerate(nums):
            if queue and queue[0] <= i - k:
                queue = queue[1:]
            while queue and nums[queue[-1]] < v:
                queue.pop()
            queue.append(i)
            if i + 1 >= k:
                ans.append(nums[queue[0]])
        return ans