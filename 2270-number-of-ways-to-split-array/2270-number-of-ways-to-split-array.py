class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:

        
        total_sum = sum(nums)
        split_ways = 0
        current_sum =0
        for index , num  in enumerate(nums[:len(nums)-1]):
            current_sum+=num

            if current_sum>= total_sum-current_sum:
                split_ways+=1

        return split_ways


        