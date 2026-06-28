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



            
        

                
        