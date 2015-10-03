import heapq
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        heap=[]
        for i in nums:
            heapq.heappush(heap,-i)
        for i in range(k):
            res=-heapq.heappop(heap)
        return res

class MinHeap:
    def __init__(self):
        self.data = []
        self.size = 0

    def parent(self, i):
        return (i-1)/2

    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2

    def add(self, num):
        self.data.append(num)
        self.size += 1
        i = self.size-1
        while i > 0 and self.data[i] < self.data[self.parent(i)]:
            tmp = self.data[self.parent(i)]
            self.data[self.parent(i)] = self.data[i]
            self.data[i] = tmp
            i = self.parent(i)

    def heapify(self, i):
        min = i
        l, r = self.left_child(i), self.right_child(i)
        if l < self.size and self.data[l] < self.data[min]:
            min = l
        if r < self.size and self.data[r] < self.data[min]:
            min = r
        if min != i:
            tmp = self.data[min]
            self.data[min] = self.data[i]
            self.data[i] = tmp
            self.heapify(min)


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    # use large top heap
    def findKthLargest(self, nums, k):
        minheap = MinHeap()
        for i in range(k):
            minheap.add(nums[i])
        for i in range(k, len(nums)):
            if nums[i] > minheap.data[0]:
                minheap.data[0] = nums[i]
                minheap.heapify(0)
        return minheap.data[0]

class Solution:
    def partition(self, l, left, right):
        if left < right:
            pivot, pivot_val = left, l[left]
            for i in range(pivot+1, right+1):
                if l[i] > pivot_val:  # ask for kth largest, sort in reverse order, not <
                    pivot += 1
                    l[i], l[pivot] = l[pivot], l[i]

            l[left], l[pivot] = l[pivot], l[left]
            return pivot
        return left

    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    # use large top heap
    def findKthLargest(self, nums, k):
        pivot = -1
        left = 0
        right = len(nums)-1
        while pivot != k-1:
            pivot = self.partition(nums, left, right)
            if pivot < k-1:
                left = pivot+1
            elif pivot > k-1:
                right = pivot-1
        return nums[pivot]

if __name__=="__main__":
    a=Solution()
    print a.findKthLargest([2, 1], 1)


from heapq import *
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    # use large top heap
    def findKthLargest(self, nums, k):
        heap = []
        for i in range(k):
            heappush(heap, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > nlargest(k, heap)[-1]:
                heappop(heap)
                heappush(heap, nums[i])
        return nlargest(k, heap)[-1]

if __name__=="__main__":
    a=Solution()
    print a.findKthLargest([-1, 2, 0],2)
    print a.findKthLargest([2000-i for i in range(2000)],1999)
    print a.findKthLargest([3,2,1,5,6,4],2)
    print a.findKthLargest([3,2,1,5,6,4],4)
    for i in range(1,7):
        print a.findKthLargest([3,2,1,5,6,4],i)


import sys
sys.setrecursionlimit(10000000)
class Solution:
    def findKthLargest(self, nums, k):
        flag,thres,i=nums[0],0,1
        while i<len(nums):
            if nums[i]>flag:
                thres+=1
                nums[thres],nums[i]=nums[i],nums[thres]
            i+=1
        nums[thres],nums[0]=nums[0],nums[thres]
        if thres+1==k:return nums[thres]
        elif thres+1>k: return self.findKthLargest(nums[:thres], k)
        else: return self.findKthLargest(nums[thres+1:], k-thres-1)
  
if __name__=="__main__":
    a=Solution()
    print a.findKthLargest([-1, 2, 0],2)
    print a.findKthLargest([2000-i for i in range(2000)],1999)
    print a.findKthLargest([3,2,1,5,6,4],2)
    print a.findKthLargest([3,2,1,5,6,4],4)
    for i in range(1,7): 
        print a.findKthLargest([3,2,1,5,6,4],i)


