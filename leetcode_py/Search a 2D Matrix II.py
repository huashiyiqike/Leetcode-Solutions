class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        row, col, width = len(matrix) - 1, 0, len(matrix[0])
        while row >= 0 and col < width:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row = row - 1
            else:
                col = col + 1
        return False


# divide and conquer, binary search
class Solution:
    def binarysearch(self, vec, target):
        left = 0
        right = len(vec) - 1
        while left <= right:
            mid = (left + right) / 2
            if vec[mid] < target:
                left = mid + 1
            elif vec[mid] > target:
                right = mid - 1
            else:
                return True
        return False

    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix or matrix[-1][-1] < target:
            return False
        if len(matrix) == 1:
            return self.binarysearch(matrix[0], target)

        if matrix[:len(matrix) / 2][-1] < target:
            return self.searchMatrix(matrix[len(matrix) / 2:], target)

        return self.searchMatrix(matrix[len(matrix) / 2:], target) or \
               self.searchMatrix(matrix[:len(matrix) / 2], target)


class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix or matrix[-1][-1] < target:
            return False
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) / 2
            if matrix[0][mid] < target:
                left = mid + 1
            elif matrix[0][mid] > target:
                right = mid - 1
            else:
                return True
        col = right + 1

        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) / 2
            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                return True
        row = right + 1

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == target:
                    return True
        return False


if __name__ == "__main__":
    a = Solution()
    print a.searchMatrix([[1, 4], [2, 5]], 5)
