class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cnt = [0]
        dp = {}
        def sol(pos,c_summ):
            
            if c_summ == target and pos==len(nums):
                cnt[0]=cnt[0]+1

            if pos == len(nums):
                return

            sol(pos+1,c_summ+nums[pos])
            sol(pos+1,c_summ-nums[pos])

            return
        sol(0,0)
        return cnt[0]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

       
        def sol(pos,val):

            if pos ==len(nums):
                if val ==0:
                    return 1
                return 0
            
            count = 0
            count+=sol(pos+1,val-nums[pos])
            count+=sol(pos+1,val+nums[pos])
                
            return count

        return sol(0,target)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

       # adding dp to it for top down approach
       # we have two vaibles to define dp state
       # as we do dfs, to while exploring other brnches we could have already solved or met perticuler state in previous explored branches , then we can use those solutions
        dp = {}
        def sol(pos,val):

            if pos ==len(nums):
                if val ==0:
                    return 1
                return 0
            if (pos,val) in dp:
                return dp[(pos,val)]

            count = 0
            count+=sol(pos+1,val-nums[pos])
            count+=sol(pos+1,val+nums[pos])
            dp[(pos,val)] = count
            return  dp[(pos,val)] 

        return sol(0,target)


    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # converting to bottom up approach
        
        # state
        # current state depends on next state
        # current state[pos,val] == next state[pos+1..], 0->1->2->3...-->n
        # base state
        # pos == len(num) and val ==0 , return 1
        # so dp[len(nums),0] = 1
        # recurrence
        # heare function call is bassically, dp state call
        #dp[(pos,val)] = dp[(pos+1,val-nums[pos])] +dp[(pos+1,val+nums[pos])]

        # ans  will be, dp[(0,target)]

        # now tricky part state is governed by (pos, val)
        # we need to find range  of possible values of the two
        # for pos ranges from (0,len(nums)), but we wwill explore it in reverse, as pos depends on pos+1
        # val, is acheive by  putting +/-, so minimum , if we pull only -,  ans max is putting + only
        # val is (-s,s), s= target

        # if perticular state is not there then we can return 0

        dp = {}
        def sol():
            S = sum(nums)
            dp[(len(nums),0)] = 1
            for pos in range(len(nums)-1,-1,-1):
                for val in range(-S, S+1):
                    dp[(pos,val)] = dp.get((pos+1,val-nums[pos]),0)+dp.get((pos+1,val+nums[pos]),0)
        
        sol()

        return dp.get((0,target),0)

    # def findTargetSumWays(self, nums: List[int], target: int) -> int:

    #     S = sum(nums)

    #     dp = {}

    #     dp[(len(nums),0)] = 1

    #     for pos in range(len(nums)-1,-1,-1):

    #         for val in range(-S,S+1):

    #             dp[(pos,val)] = (
    #                 dp.get((pos+1,val-nums[pos]),0)
    #                 +
    #                 dp.get((pos+1,val+nums[pos]),0)
    #             )

    #     return dp.get((0,target),0)

    


    



            
        

                
        