
# Memoized
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def getmaxProfit(prices, start, end, is_buy):

            if start == end:
                return 0

            if (start, end, is_buy) in dp:
                return dp[(start, end, is_buy)]

            local_max = 0

            for i in range(start, end):

                if is_buy:
                    local_max = max(local_max, getmaxProfit(prices, i, end, 0))
                else:
                    pr = prices[i] - prices[start]

                    if pr > 0:
                        p = pr + getmaxProfit(prices, i + 1, end, 1)

                        local_max = max(local_max, p)

            dp.update({(start, end, is_buy): local_max})
            return local_max
