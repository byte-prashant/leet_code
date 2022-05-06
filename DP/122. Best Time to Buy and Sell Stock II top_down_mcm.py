
# Memoized
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def getmaxProfitmcm(prices, start, end):

            if end <= start:
                return 0

            local_max = 0

            if (start, end) in dp:
                return dp[(start, end)]
            for i in range(start, end):
                for j in range(i + 1, end):
                    if prices[j] - prices[i] > 0:
                        profit = prices[j] - prices[i] + getmaxProfitmcm(prices, start, i - 1) + \
                                 getmaxProfitmcm(prices, j + 1, end)
                        local_max = max(profit, local_max)
            dp.update({(start, end): local_max})
            return local_max

        return getmaxProfitmcm(prices, 0, len(prices))
