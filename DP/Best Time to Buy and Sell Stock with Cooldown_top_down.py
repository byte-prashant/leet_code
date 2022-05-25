class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        end = len(prices)
        dp = {}

        def maxProfitSol(i, is_buy):

            if i >= end:
                return 0

            if (i, is_buy) in dp:
                return dp[(i, is_buy)]

            if is_buy:
                local_max = max(-prices[i] + maxProfitSol(i + 1, 0), maxProfitSol(i + 1, 1))

            else:
                local_max = max(prices[i] + maxProfitSol(i + 2, 1), maxProfitSol(i + 1, 0))

            dp.update({(i, is_buy): local_max})

            return local_max

        return maxProfitSol(0, 1)
