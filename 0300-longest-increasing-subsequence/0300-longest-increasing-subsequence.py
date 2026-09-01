class Solution:
   
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(pos, prev):

            if pos == len(nums):
                return 0

            skip = dfs(pos + 1, prev)

            take = 0
            if prev == -1 or nums[pos] > nums[prev]:
                take = 1 + dfs(pos + 1, pos)

            return max(skip, take)

        return dfs(0, -1)

    
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def dfs(pos, prev):

            if pos == len(nums):
                return 0

            if (pos,prev) in dp:
                return dp[(pos,prev)]

            skip = dfs(pos + 1, prev)

            take = 0
            if prev == -1 or nums[pos] > nums[prev]:
                take = 1 + dfs(pos + 1, pos)
            dp[(pos,prev)] = max(skip,take)
            return dp[(pos,prev)]

        return dfs(0, -1)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def sol(pos): 
            if pos in dp:
                return dp[pos]    
            if pos>=len(nums):
                return 0
            c = 0
            for i in range(pos+1,len(nums)):
                if nums[i]>nums[pos]:
                    c = max(c ,sol(i)+1)
            dp[pos] = c
            return c
        c = 0
        for pos in range(len(nums)):
             c = max(c ,sol(pos)+1)
        return c



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = {}

        def sol(pos, count):

            if pos>=len(nums):
                return count

            if (pos, count) in dp:
                return dp[(pos,count)]

            c = count
            for index in range(pos+1, len(nums)):

                if nums[index]> nums[pos]:
                    c = max(c,sol(index,count+1))

            dp[(pos,count)] = c


            return dp[(pos, count)]

        c = 0

        for pos in  range(len(nums)):
            c = max(c, sol(pos,1))

        return c

            

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = {}

        def sol(pos):
            if pos in dp:
                return dp[pos]

            best = 1

            for index in range(pos + 1, len(nums)):
                if nums[index] > nums[pos]:
                    best = max(best, 1 + sol(index))

            dp[pos] = best
            return best

        ans = 0

        for pos in range(len(nums)):
            ans = max(ans, sol(pos))

        return ans      
        