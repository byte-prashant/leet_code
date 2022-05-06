class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        largest = prices[len(prices) - 1]
        for i in range(0, len(prices)):
            ele = prices[len(prices) - 1 - i]
            if max_prof < -ele + largest:
                max_prof = -ele + largest

            if ele > largest:
                largest = ele

        return max_prof
