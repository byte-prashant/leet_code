class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def partition(pos,total):
            if len(nums) == pos:
                if total ==0:
                    return True
                return False


            return partition(pos+1,total-nums[pos]) or partition(pos+1,total+nums[pos])

        #return partition(0,0)


        # use memoization
        # this is giving us memomry limit
        dp = {}
        def partition(pos,total):
            if len(nums) == pos:
                if total ==0:
                    return True
                return False
            if len(nums) < pos:
                return False

            if (pos,total) in dp:
                return dp[(pos,total)]

            dp[(pos,total)] = partition(pos+1,total-nums[pos]) or partition(pos+1,total+nums[pos])
            return dp[(pos,total)]

        return partition(0,0)


    def canPartition(self, nums: List[int]) -> bool:
        # instead of exloring all combination, where target is 0
        # we can make our target  = total//2
        # this way we need to selct few elements
        # saving memory
        def partition(pos,total):
            # if summ becomes less than zero, no need to explore
            # as all remaining elements are positive
            if total<0:
                return False
            if len(nums) == pos:
                if total ==0:
                    return True
                return False
            
            # selecting  and not selectin

            return partition(pos+1,total-nums[pos]) or partition(pos+1,total)

        target = sum(nums)

        if target%2 ==1:
            return False

        new_target = target//2

        return partition(0,new_target)


    def canPartition(self, nums: List[int]) -> bool:
        # instead of exloring all combination, where target is 0
        # we can make our target  = total//2
        # this way we need to selct few elements
        # saving memory
        dp = {}
        def partition(pos,total):
            # if summ becomes less than zero, no need to explore
            # as all remaining elements are positive
            if total<0:
                return False
            if len(nums) == pos:
                if total ==0:
                    return True
                return False
            
            # selecting  and not selectin
            if (pos, total) in dp:
                return dp[(pos,total)]

            dp[(pos,total)] = partition(pos+1,total-nums[pos]) or partition(pos+1,total)
            return dp[(pos,total)]

        target = sum(nums)

        if target%2 ==1:
            return False

        new_target = target//2

        return partition(0,new_target)

        def canPartition(self, nums: List[int]) -> bool:
            # conerting to bottom up
            # if no state, (pos,total) then return False

            # state ==> (pos,total)

            # base dp[(len(nums),0)] = True

            # recurrence
            #dp[(pos,total)] = dp[(pos+1,total-nums[pos])] or dp[(pos+1,total)]

            # loop
            # two var --> two loops
            # ranges for loop
            # pos => (0, len(nums)), total = (min, max) ==> (every value is selected, no seected) ==(total-(summ),total)
       
            dp = {}
           

            target = sum(nums)

            if target%2 ==1:
                return False

            new_target = target//2
            dp[(len(nums),0)] = True
            
            # as pos depends on pos+1
            for pos in range(len(nums)-1,-1,-1):
                for total in range(new_target-sum(nums), new_target+1):
                     dp[(pos,total)] = dp.get((pos+1,total-nums[pos]),False) or dp.get((pos+1,total),False)


            return dp.get((0,new_target),False)

    


            
        