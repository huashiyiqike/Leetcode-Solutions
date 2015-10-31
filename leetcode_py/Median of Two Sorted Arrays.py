class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if len(A) > len(B):
            A, B = B, A
        if len(A) == 0:
            if len(B) == 0:
                return 0.0
            return (B[(len(B) - 1) / 2] + B[len(B) / 2]) / 2.0

        k = (len(A) + len(B) - 1) / 2 + 1
        left, right = 0, len(A)
        while left < right:
            mid = (left + right) / 2
            j = k - mid - 1
            if j < 0:
                break
            if j >= len(B) or A[mid] < B[j]:
                left = mid + 1
            else:  # A[mid] >= B[j]
                right = mid

                # A[left] > B[k-left-1]  total k + 1 numbers

        aminus = A[left - 1] if left >= 1 else -1 << 64
        bj = B[k - left - 1] if k - left - 1 >= 0 else -1 << 64
        m = max(aminus, bj)

        if (len(A) + len(B)) % 2 == 0:
            ai = A[left] if left < len(A) else 1 << 64
            bjplus = B[k - left] if k - left < len(B) else 1 << 64
            n = min(ai, bjplus)
            return (m + n) / 2.0
        else:
            return m

# not O(lgn)
# class Solution:
#     # @return a float
#     def findMedianSortedArrays(self, A, B):
#         i, j = 0, 0
#         c = []
#         while i < len(A) and j < len(B):
#             if A[i] < B[j]:
#                 c.append(A[i])
#                 i += 1
#             else:
#                 c.append(B[j])
#                 j += 1
#         c += A[i:]
#         c += B[j:]
#         return (c[(len(A) + len(B) - 1) / 2] + c[(len(A) + len(B)) / 2]) / 2.0
#

if __name__ == '__main__':
    a = Solution()
    A = [4, 5, 6]
    B = [1, 2, 3, 4, 5]

    print a.findMedianSortedArrays(A, B)
# https://leetcode.com/discuss/20897/intuitive-python-solution-smallest-two-sorted-arrays-252ms
