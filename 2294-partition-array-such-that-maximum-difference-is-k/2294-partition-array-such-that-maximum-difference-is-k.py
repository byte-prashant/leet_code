class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:

        ans =0
        nums.sort()
        first = nums[0]
        for num in nums:
            if num-first>k:
                ans+=1
                first = num
        return ans+1

        