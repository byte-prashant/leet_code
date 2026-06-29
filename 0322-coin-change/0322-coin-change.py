class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minn = [float("inf")]
        def coin(pos, amount,count):
            if amount<0:
                return 
            if amount == 0:
                minn[0] = min(minn[0],count)

            if pos >= len(coins):
                return

            
            coin(pos+1, amount,count)
            coin(pos, amount-coins[pos],count+1)
            coin(pos+1, amount-coins[pos],count+1)

            return

        coin(0, amount,0)
        return -1 if minn[0] == float("inf") else minn[0]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minn = [float("inf")]
        # converting to top down approach
        #  we  each state  is reprented by  three vars
        # can we remove any of the var, wich is unnecessary

        dp = {}
        def coin(pos, amount):
            if amount<0:
                return float("inf") # return inf coins
            if amount == 0:
                return 0 # no further coins

            if pos >= len(coins):
                return float("inf") # return inf coins

            
            skip = coin(pos+1, amount)
            take = coin(pos, amount-coins[pos])+1
            #coin(pos+1, amount-coins[pos],count+1)

            return min(skip, take)

        ans = coin(0, amount)
        return -1 if ans == float("inf") else ans



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minn = [float("inf")]
        # converting to top down approach
        #  we  each state  is reprented by  two vars
        # count has been removed
        # 

        dp = {}
        def coin(pos, amount):
            if amount<0:
                return float("inf") # return inf coins
            if amount == 0:
                return 0 # no further coins

            if pos >= len(coins):
                return float("inf") # return inf coins
            if (pos, amount) in dp:
                return dp[(pos, amount)]
            
            skip = coin(pos+1, amount)
            take = coin(pos, amount-coins[pos])+1
            #coin(pos+1, amount-coins[pos],count+1)
            dp[(pos, amount)] = min(skip, take)
            return dp[(pos, amount)]

        ans = coin(0, amount)
        return -1 if ans == float("inf") else ans



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minn = [float("inf")]
        # converting to bottom up
        #  we  each state  is reprented by  two vars
        # count has been removed
        #  state pos depends on  pos+1
        # state reprensented by (pos, amount)
        # pos ==> range(0, len(coins)), amount => range(min, max) ==> min =>  we continuous decreasing from amoun,  minimum amout will be if we decreat it by max value of coin by n time
        # min  = amount - (n* max(coins))
        # but as all amount <0 has been ignored, we can start loop from 1 to amount
        # maxx. = if we do not minimize anything, amount itself


        #amount = (amount - (n* max(coins)),amount)

        # recurrent
        # dp[(pos+1, amount)], dp[(pos+1, amount-coins[pos])]

        # base 
        #  by default 0, whenever amount ==0, return zero, if less than zeo, it is inf

        # we can use matrix or dict anything

        dp = {}
        
        for pos in range(len(coins)-1,-1,-1):
            dp[(pos,0)] = 0
        for amt in range(1, amount + 1): 
            dp[(len(coins), amt)] = float("inf")
        for pos in range(len(coins)-1,-1,-1):
            for amount in range(1 ,amount+1):
                skip = dp.get((pos+1, amount),float("inf"))
                if amount >= coins[pos]: 
                    take = dp.get((pos, amount - coins[pos]),float("inf")) + 1 
                else: 
                    take = float("inf")
                    #coin(pos+1, amount-coins[pos],count+1)
                dp[(pos, amount)] = min(skip, take)
                    

        ans = dp.get((0, amount),float("inf"))
        return -1 if ans == float("inf") else ans


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minn = [float("inf")]
        # converting to bottom up
        #  we  each state  is reprented by  two vars
        # count has been removed
        #  state pos depends on  pos+1
        # state reprensented by (pos, amount)
        # pos ==> range(0, len(coins)), amount => range(min, max) ==> min =>  we continuous decreasing from amoun,  minimum amout will be if we decreat it by max value of coin by n time
        # min  = amount - (n* max(coins))
        # but as all amount <0 has been ignored, we can start loop from 1 to amount
        # maxx. = if we do not minimize anything, amount itself


        #amount = (amount - (n* max(coins)),amount)

        # recurrent
        # dp[(pos+1, amount)], dp[(pos+1, amount-coins[pos])]

        # base 
        #  by default 0, whenever amount ==0, return zero, if less than zeo, it is inf

        # we can use matrix or dict anything


        # using mattrix instead of dict
        # how to choose, row and colum
        dp = [[float("inf") for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        
        for pos in range(len(coins)-1,-1,-1):
            dp[pos][0] = 0
        for amt in range(1, amount + 1): 
            dp[len(coins)] [amt] = float("inf")

        for pos in range(len(coins)-1,-1,-1):
            for amount in range(1 ,amount+1):
                skip = dp[pos+1][ amount]
                if amount >= coins[pos]: 
                    take = dp[pos][ amount - coins[pos]] + 1 
                else: 
                    take = float("inf")
                    #coin(pos+1, amount-coins[pos],count+1)
                dp[pos][amount] = min(skip, take)
                    

        ans = dp[0][amount]
        return -1 if ans == float("inf") else ans
            


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minn = [float("inf")]
        # previous solution
        # every new state is depent on current row ==> pos, and previous row
        # so we need not to, have all roow, cuurent and preev row is suffices

        # 
        next_row = [float("inf") for _ in range(amount + 1)]
        current_row = [float("inf") for _ in range(amount + 1)]
        
     
        next_row[0] = 0
       
        for pos in range(len(coins)-1,-1,-1):
            # in prv sol we initiliazed zero for each row
            current_row[0] = 0
            for amt in range(1 ,amount+1):
                skip = next_row[ amt]
                if amt >= coins[pos]: 
                    take = current_row[ amt - coins[pos]] + 1 
                else: 
                    take = float("inf")
                    #coin(pos+1, amount-coins[pos],count+1)
                current_row[amt] = min(skip, take)
                    
            # current set as new
            next_row = current_row[:]
            current_row = [float("inf")] * (amount + 1)

        
        ans =next_row[amount]
        return -1 if ans == float("inf") else ans



# Instead of asking

# What is the answer using coins starting from index pos?

# Ask

# What is the minimum coins needed to make amount x?

#  also  dp state saves no.  of coins for each amount, and we can use it
# for each amount, we should calculate all  minum,  required coins
# We're simply changing the loop order.

# current state (pos, amount) says Minimum coins needed to make amount using only coins from index pos onward.

# now we will say, minimum coin needed  for amount, using all coins
# now we need to to track for range of coins used  as we are exploring all coins now

# so we can convert all state (pos, amount) to (amount) only

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp= [float("inf")] * (amount+1)
        dp[0]= 0
        for amnt in range(1, amount+1):
                for coin in coins:
                    if amnt-coin >= 0:
                        dp[amnt]= min(dp[amnt], 1+ dp[amnt-coin])
        return dp[amount] if dp[amount]!= float("inf") else  -1