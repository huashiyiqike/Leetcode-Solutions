class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        head = 0
        for i in range(len(A) - 1):
            if A[i + 1] != A[head]:
                head += 1
                A[head] = A[i + 1]

        A = A[:head + 1]
        return head + 1


if __name__ == "__main__":
    a = Solution()
    print a.removeDuplicates([])
    print a.removeDuplicates([1, 1, 2, 2, 3])
