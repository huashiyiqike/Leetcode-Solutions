class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res <<= 1
            if n & 1:
                res |= 1
            n >>= 1

        return res


if __name__ == "__main__":
    a = Solution()
    print a.reverseBits(43261596)
