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
