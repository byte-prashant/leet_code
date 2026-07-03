class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        def sol(pos, amount):

            if pos>=len(coins):
                return []
            if amount<0:
                return []
            if amount ==0:
                return [[]]

            result = []
            for index in range(pos,len(coins)):

                sub_list = sol(index,amount-coins[index])

                for ele in sub_list:
                   
                    result.append(ele +[coins[index]])
            return result

        ans = sol(0,amount)


        return len(ans) if ans else 0

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}
        def sol(pos, amount):

            if pos>=len(coins):
                return []
            if amount<0:
                return []
            if amount ==0:
                return [[]]
            if (pos,amount) in dp:
                return dp[(pos,amount)]
            result = []
            for index in range(pos,len(coins)):

                sub_list = sol(index,amount-coins[index])

                for ele in sub_list:
                   
                    result.append(ele +[coins[index]])
            dp[(pos,amount)] = result
            return result

        ans = sol(0,amount)


        return len(ans) if ans else 0

# previous on memory limit exceede
# balow one time limit exceeded

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}
        def sol(pos, amount):

            if pos>=len(coins):
                return 0
            if amount<0:
                return 0
            if amount ==0:
                return 1
            if (pos,amount) in dp:
                return dp[(pos,amount)]
            result = 0
            for index in range(pos,len(coins)):
                if (index,amount-coins[index]) in dp:
                    result+= dp[(index,amount-coins[index])]
                else:   
                    result += sol(index,amount-coins[index])

            dp[(pos,amount)] = result
            return result

        ans = sol(0,amount)


        return ans if ans else 0

# Because this loop executes for every (pos, amount) DP state, your algorithm becomes O(amount × n²) rather than the optimal O(amount × n).

# So the issue is not recursion, not memoization, and not the dictionary lookup—it's the extra loop inside each memoized state that repeatedly scans all remaining coins.

# every parent still has to iterate over the whole remaining coin list before discovering the memoized result.

# Memoization removes repeated computation,

# but not repeated looping

#suppose we have 1,2,3,4,5,6 coins
# in above solution we are trying all combination starting with 1 then 2 a..... then 5 and ..
# think terms if coin can bet icluded or not

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}
        def sol(pos, amount):

            if amount == 0:
                return 1

            if pos>=len(coins):
                return 0

            if amount<0:
                return 0
            
            if (pos,amount) in dp:
                return dp[(pos,amount)]
            result = 0
            included = sol(pos,amount-coins[pos])
            exculded = sol(pos+1,amount)

            dp[(pos,amount)] = included+exculded
            return dp[(pos,amount)] 

        ans = sol(0,amount)


        return ans if ans else 0


# convertion to bottom up

# pos range(0, len(coins)) # amount  range(0, amount+1)
# base state, for each coin when, amount 0,  value 1
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [[0 for i in range(amount+1)] for _  in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1

        for coin in range(len(coins)-1,-1,-1):
            for amnt in range(amount+1):
                included=0
                if amnt >= coins[coin]:
                    included = dp[coin][amnt-coins[coin]]
                exculded = dp[coin+1][amnt]

                dp[coin][amnt] = included+exculded
        
        return dp[0][amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)

        next = [0] * (amount + 1)
        next[0] = 1

        for coin in range(n - 1, -1, -1):

            current = [0] * (amount + 1)
            current[0] = 1

            for amt in range(1, amount + 1):

                included = 0
                if amt >= coins[coin]:
                    included = current[amt - coins[coin]]

                excluded = next[amt]

                current[amt] = included + excluded

            next = current

        return next[amount]    
        
        