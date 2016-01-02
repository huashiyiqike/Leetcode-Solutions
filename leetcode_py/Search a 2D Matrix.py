class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) / 2
            tmp = matrix[mid / len(matrix[0])][mid % len(matrix[0])]
            if target < tmp:
                right = mid - 1
            elif target > tmp:
                left = mid + 1
            else:
                return True
        return False


class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        left = 0
        right = len(matrix) - 1
        row = 0
        while left <= right:
            mid = (left + right) / 2
            if target < matrix[mid][0]:
                right = mid - 1  # or mid
            elif target > matrix[mid][0]:
                left = mid + 1
            else:
                return True
        if right < 0:
            return False

        left = 0
        row = right
        right = len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) / 2
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True

        return False


if __name__ == "__main__":
    a = Solution()
    print a.searchMatrix([[1]], 0)
    print a.searchMatrix([[1], [3]], 1)
    print a.searchMatrix([[1, 2], [3, 4]], 2)
    print a.searchMatrix([[1, 2], [3, 4], [5, 6]], 5)

# https://leetcode.com/discuss/15379/binary-search-on-an-ordered-matrix
