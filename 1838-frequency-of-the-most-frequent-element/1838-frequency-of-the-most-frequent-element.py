class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        current_sum =0
        left =0 
        max_val = float("-inf")
        for right in range(len(nums)):
            current_sum+=nums[right]

            while k< (nums[right]*(right-left+1))-current_sum:

                current_sum-=nums[left]
                left+=1

            max_val = max(max_val,right-left+1)

        return max_val