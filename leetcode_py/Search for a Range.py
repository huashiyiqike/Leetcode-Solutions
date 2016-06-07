class Solution:
    def binsearch(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid, mid
        return left, right

    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        left = self.binsearch(nums, target - 0.5)[1] + 1
        right = self.binsearch(nums, target + 0.5)[0] - 1
        if left >= len(nums) or (left < len(nums) and nums[left] != target):
            return [-1, -1]

        return [left, right]


#
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, arr, target):
        start = self.binary_search(arr, target - 0.5)
        if arr[start] != target:
            return [-1, -1]
        arr.append(0)
        end = self.binary_search(arr, target + 0.5) - 1
        return [start, end]

    def binary_search(self, arr, target):
        start, end = 0, len(arr) - 1
        while start < end:
            mid = (start + end) // 2
            if target < arr[mid]:
                end = mid
            else:
                start = mid + 1
        return start


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) / 2
            if A[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        ll = l
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) / 2
            if A[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        rr = r
        if ll <= rr:
            return [ll, rr]
        else:
            return [-1, -1]


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        key = target
        if len(A) == 0:
            return [-1, -1]
        if len(A) == 1:
            if target != A[0]:
                return [-1, -1]
            else:
                return [0, 0]
        l, r, p1, p2 = 0, len(A) - 1, -1, -1
        while l < r:
            mid = (l + r) / 2
            if target < A[mid]:
                r = mid
            elif target > A[mid]:
                l = mid - 1
            elif target == A[mid]:
                l = mid
                break
            if l + 2 >= r:
                break
        if A[r] == target:
            p1 = r
        elif A[l] == target:
            p1 = l
        else:
            return [-1, -1]

        l = p1
        r = len(A) - 1
        while l < r:
            mid = (l + r) / 2
            if target < A[mid]:
                r = mid + 1
            elif target > A[mid]:
                l = mid
            elif target == A[mid]:
                r = mid
                break
            if l + 2 >= r:
                break

        if A[r] == target:
            p2 = r
        elif A[l] == target:
            p2 = l
        else:
            return [-1, -1]
        return [p1, p2]

# class Solution:
#     # @param A, a list of integers
#     # @param target, an integer to be searched
#     # @return a list of length 2, [index1, index2]
#     def searchRange(self, A, target):
#         key = target
#         if len(A) == 0 :
#             return [-1, -1]
#         if len(A) == 1:
#             if target != A[0]:
#                 return [-1, -1]
#             else:
#                 return [0, 0]
#                 
#         l = 0
#         r = len(A) - 1
#         while l < r:
#             mid = (l + r) >> 1
#             if A[mid] > key:
#                 r = mid - 1
#             elif A[mid] == key:
#                 r = mid
#             elif A[mid] < key:
#                 l = mid
#             if l + 1 == r:
#                 break
#         if A[l] == key:
#             p1 = l
#         elif A[r] == key:
#             p1 = r
#         else:
#             return [-1, -1]
#         
#         l = p1
#         r = len(A) - 1
#         while l < r:
#             mid = (l + r) >> 1
#             if A[mid] > key:
#                 r = mid - 1
#             elif A[mid] < key:
#                 l = mid + 1 
#             elif A[mid] == key:
#                 l = mid
#             if l + 1 == r:
#                 break
# 
#         if A[r] == key:
#             p2 = r
#         elif A[l] == key:
#             p2 = l
#         else:
#             return [-1, -1]
#             
#         return [p1, p2]       

if __name__ == '__main__':
    a = Solution()
    num = [0, 0, 1, 1, 2, 2]

    print a.searchRange(num, 0)
    num = [5, 7, 7, 8, 8, 10]
    print a.searchRange(num, 8)

#
