class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        for i in range(len(matrix) / 2):
            for j in range(len(matrix[0])):
                matrix[len(matrix) - 1 - i][j], matrix[i][j] = matrix[i][j], matrix[len(matrix) - 1 - i][j]

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution:
    def rotate(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]
