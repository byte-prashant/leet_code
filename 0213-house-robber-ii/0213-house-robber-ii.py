class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
                return nums[0]

        if len(nums)==2:
            return max(nums)
        def sol(houses):
            

            dp = [0]*len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0],houses[1])

            for i , num in enumerate(houses):
                if i<2:
                    continue
               
                dp[i] = max(dp[i-1],houses[i]+dp[i-2])

            return dp[len(houses)-1]
               
        # exclude first and then last
        return max(sol(nums[:-1]),sol(nums[1:]))
          

        