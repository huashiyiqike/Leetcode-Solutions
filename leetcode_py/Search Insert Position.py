class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left


class Solution:
    def f(self, nums, target, left, right):
        if left > right:
            return right + 1
        mid = (left + right) / 2
        if nums[mid] > target:
            return self.f(nums, target, left, mid - 1)
        elif nums[mid] < target:
            return self.f(nums, target, mid + 1, right)
        else:
            return mid

    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        return self.f(nums, target, 0, len(nums) - 1)


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        index = 0
        while target > A[index]:
            index += 1
            if index >= len(A):
                return index
        return index


class Solution:
    def searchInsert(self, A, target):
        return self.searchInsertRecur(A, target, 0, len(A) - 1)

    def searchInsertRecur(self, A, target, low, high):
        mid = (high + low) / 2
        if low > high:
            return low
        if A[mid] == target:
            return mid
        if A[mid] < target:
            return self.searchInsertRecur(A, target, mid + 1, high)
        else:
            return self.searchInsertRecur(A, target, low, mid - 1)

            # def searchInsert(self, A, target):
            #   """Iterative solution is also fine.
            #   """
            #     low, high = 0, len(A) - 1
            #     while low <= high:
            #         mid = (low + high) / 2
            #         if A[mid] == target:
            #             return mid
            #         elif A[mid] < target:
            #             low = mid + 1
            #         else:
            #             high = mid - 1
            #     return low
