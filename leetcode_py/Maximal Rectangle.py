class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        h, w = len(matrix), len(matrix[0])
        m = [[0] * w for _ in range(h)]
        for j in range(h):
            for i in range(w):
                if matrix[j][i] == '1':
                    m[j][i] = m[j - 1][i] + 1  # not only convert but accumulate height
        return max(self.largestRectangleArea(row) for row in m)

    def largestRectangleArea(self, height):
        height.append(0)
        stack, size = [], 0
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                size = max(size, h * w)
            stack.append(i)
        return size


from copy import deepcopy
class Solution:
    def f(self, m2, row):
        stack = []
        v = deepcopy(m2[row])
        v.append(0)
        res = 0
        i = 0
        while i < len(v):
            if len(stack) == 0 or (len(stack) > 0 and v[stack[-1]] < v[i]):
                stack.append(i)
                i += 1
            else:
                h = v[stack.pop()]
                if len(stack) > 0:
                    res = max(res, h * (i - stack[-1] - 1))
                else:
                    res = max(res, h * i)
        return res

    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        m2 = [[0 for i in j] for j in matrix]
        for i in range(len(matrix)):
            matrix[i] = map(lambda x: int(x), list(matrix[i]))

            # print matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    m2[i][j] = 1
                    for k in range(i + 1, len(matrix)):
                        if matrix[k][j] == 1:
                            m2[i][j] += 1
                        else:
                            break
        res = 0
        for i in range(len(m2)):
            res = max(res, self.f(m2, i))
        return res


if __name__ == "__main__":
    a = Solution()
    print a.maximalRectangle(["01101", "11010", "01110", "11110", "11111", "00000"])
    print a.maximalRectangle(["11111111", "11111110", "11111110", "11111000", "01111000"])

    print a.maximalRectangle(['111', '011'])
    print a.maximalRectangle([['0', '1'], ['1', '1']])
    print a.maximalRectangle([['1'], ['0'], ['1'], ['1']])
    print a.maximalRectangle([['1'], ['1'], ['0'], ['1']])
    print a.maximalRectangle([['1', '0'], ['1', '1']])

    print a.maximalRectangle([['1', '1'], ['1', '0']])

    print ""

    print a.maximalRectangle([['1']])
    print a.maximalRectangle([['1'], ['0']])

    print a.maximalRectangle([['1'], ['1'], ['1'], ['1']])
    print a.maximalRectangle([['1', '1'], ['1', '1']])
