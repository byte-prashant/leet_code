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

            

        