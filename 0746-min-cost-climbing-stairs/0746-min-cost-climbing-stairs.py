class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        def recursive(n):
            if n<0:
                return 0

            if n==0 or n==1:
                return cost[n] 

            
            return cost[n] + min(recursive(n-1),recursive(n-2))

        
        return min(recursive(len(cost)-1),recursive(len(cost)-2))


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = {}
        def recursive(n):
            if n<0:
                return 0

            if n==0 or n==1:
                return cost[n] 
            if n in dp:
                return dp[n]
            
            dp[n]  = cost[n] + min(recursive(n-1),recursive(n-2))

            return dp[n]

        
        return min(recursive(len(cost)-1),recursive(len(cost)-2))