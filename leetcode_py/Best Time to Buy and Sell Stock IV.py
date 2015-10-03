class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        # for saving memory
        if k >= len(prices) / 2:
            result = 0
            for index, item in enumerate(prices):
                if index + 1 < len(prices):
                    if prices[index] < prices[index + 1]:
                        result += prices[index + 1] - prices[index]
            return result

        locals = [0 for _ in range(k + 1)]
        globals = [0 for _ in range(k + 1)]
        for i in range(1, len(prices)):
            for j in range(k, 0, -1):
                tmp = prices[i] - prices[i - 1]
                # local must sell at each jth transaction
                locals[j] = max(locals[j] + tmp, globals[j - 1] + max(0, tmp))
                globals[j] = max(globals[j], locals[j])

        return globals[-1]


if __name__ == "__main__":
    a = Solution()
    print a.maxProfit(2, [6, 1, 3, 2, 4, 7])
    print a.maxProfit(2, [1, 6, 1, 3, 2, 4, 7])
    #
    # #MLE
    # class Solution:
    #     # @param {integer} k
    #     # @param {integer[]} prices
    #     # @return {integer}
    #     def maxProfit(self, k, prices):
    #         if len(prices)==0:
    #             return 0
    #         locals=[[ 0 for j in range(k+1)] for i in range(len(prices))]
    #         globals=[[ 0 for j in range(k+1)] for i in range(len(prices))]
    #
    #         for i in range(1,len(prices)):
    #             for j in range(1,k+1):
    #                 locals[i][j]=max(locals[i-1][j-1]+prices[i]-prices[i-1],globals[i-1][j-1]+max(0,prices[i]-prices[i-1]))
    #                 globals[i][j]=max(globals[i-1][j],locals[i][j])
    #         return globals[-1][-1]
    # http://www.cnblogs.com/EdwardLiu/p/4008162.html
