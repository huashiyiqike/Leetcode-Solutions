class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        result = 0
        for index, item in enumerate(prices):
            if index + 1 < len(prices):
                if prices[index] < prices[index + 1]:
                    result += prices[index + 1] - prices[index]
        return result
