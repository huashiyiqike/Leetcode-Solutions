class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices:
            return 0
        forward = [0] * (len(prices))
        mins = prices[0]
        for idx, item in enumerate(prices[1:], start=1):
            mins = min(mins, item)
            forward[idx] = max(item - mins, forward[idx - 1])

        maxs = prices[-1]
        res = 0
        for idx in range(len(prices) - 2, -1, -1):
            maxs = max(maxs, prices[idx])
            res = max(res, maxs - prices[idx] + forward[idx])  # not forward[idx+1] cannot sell and buy at the same day
        return res

#
# class Solution:
#     # @param {integer[]} prices
#     # @return {integer}
#     def maxProfit(self, prices):
#         if len(prices)==0:
#             return 0
#         forward=[0]
#         mins=prices[0]
#         for idx,item in enumerate(prices[1:]):
#             mins = min(mins,item)
#             forward.append(max(forward[-1],item-mins))
#
#        # print forward
#         maxs=prices[-1]
#         res=0
#         for idx in range(len(prices)-1,-1,-1):
#             maxs=max(maxs,prices[idx])
#             res=max(res,forward[idx]+maxs-prices[idx])
#         return res

if __name__ == "__main__":
    a = Solution()
    print a.maxProfit([2, 5, 1, 6])
    print a.maxProfit([1, 2, 1, 1, 2])
    print a.maxProfit([1])
