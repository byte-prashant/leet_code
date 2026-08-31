class Solution:
    def rob(self, nums: List[int]) -> int:

        # as we are chosing alternate we have two possible sequence
       # startng from 0 and starting from 1

        if len(nums) ==1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        

        last_rob = nums[0]
        adj = max_amount = max(nums[0],nums[1])

        for index, num in enumerate(nums):
            if index<2:
                continue

            current_rob = last_rob+num
            current_max = max(current_rob,adj)
            max_amount = max(max_amount,current_max)
            last_rob = adj
            adj = current_max

        return max_amount


class Solution:
    def rob(self, nums: List[int]) -> int:


        def sol(pos, is_nieghbour_selected):

            if pos >=len(nums):
                return 0


            #return sol(pos+1, 1) if is_nieghbour_selected else max(sol(pos+1, 1)+nums[pos],sol(pos+1, 0))

            if is_nieghbour_selected:
                return sol(pos+1,0)

            return max(sol(pos+1,1)+nums[pos], sol(pos+1,0))

        return sol(0,0)

class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = {}
        def sol(pos, is_nieghbour_selected):

            if pos >=len(nums):
                return 0

            if (pos,is_nieghbour_selected) in dp:
                return dp[(pos,is_nieghbour_selected)]


            #return sol(pos+1, 1) if is_nieghbour_selected else max(sol(pos+1, 1)+nums[pos],sol(pos+1, 0))

            if is_nieghbour_selected:
                dp[(pos,is_nieghbour_selected)] = sol(pos+1,0)
                return dp[(pos,is_nieghbour_selected)]

            dp[(pos,is_nieghbour_selected)] = max(sol(pos+1,1)+nums[pos], sol(pos+1,0))

            return dp[(pos,is_nieghbour_selected)]

        return sol(0,0)
