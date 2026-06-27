class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        def n_ways(step):
            if step ==0:
                return 1
            if step<0:
                return 0
            if step in dp:
                return dp[step]
            dp[step] = n_ways(step-1)+n_ways(step-2)

            return dp[step]

        return n_ways(n)
            