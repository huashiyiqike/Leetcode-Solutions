import sys


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        mins = sys.maxint
        res = 0
        for i in prices:
            if i < mins:
                mins = i
            res = max(res, i - mins)
        return res


class Solution:
    def maxProfit(self, prices):
        locals = 0
        globals = 0
        for i in range(1, len(prices)):
            locals = max(prices[i] - prices[i - 1] + locals, prices[i] - prices[i - 1])
            globals = max(locals, globals)
        return globals
