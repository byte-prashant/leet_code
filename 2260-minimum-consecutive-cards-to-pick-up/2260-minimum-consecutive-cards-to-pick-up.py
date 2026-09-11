class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        dp = {}
        ans = float("+inf")
        for index, val in enumerate(cards):

            if val in dp:
                ans =  min(ans, index-dp[val]+1)

            dp[val] = index

        if ans == float("+inf"):
            return -1

        return ans
        

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dp = {}
        ans = float("+inf")

        for index, val in enumerate(cards):
            if val in dp:
                ans = min(ans,-dp[val]+index +1)

            dp[val] = index

        if ans == float("+inf"):
            return -1

        return ans