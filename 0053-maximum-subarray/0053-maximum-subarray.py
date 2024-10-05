class Solution:


    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                max_sum = max(max_sum, sum(nums[i:j+1]))

        
        return max_sum


    def maxSubArray(self, nums: List[int]) -> int:

        summ = 0
        maxx = float("-inf")
        for ele in nums:
            summ  = max(ele,summ+ele)
            maxx = max(summ, maxx)
        
        return maxx



        