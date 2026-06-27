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

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #dp = {}

        # in yop down approach all dp states are represneted by one variable
        # so we can explore all state in single loop
        # converting to bootom up approach
        dp = [0]*(len(cost)+1)
         #init base case
        dp[0] = cost[0]
        dp[1] = cost[1]
        n = len(cost)
        # now exploring all states
        for state in range(2,len(cost)):
            print(state)
            dp[state] = cost[state] + min(dp[state-1],dp[state-2])

        return min(dp[n-1],dp[n-2])
       

        
    