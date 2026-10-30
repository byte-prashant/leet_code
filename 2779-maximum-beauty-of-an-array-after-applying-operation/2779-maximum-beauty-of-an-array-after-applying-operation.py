class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        nums.sort()
        current = 1
        ans = 1
        left = 0
        prev = nums[left]+k
        for pos in range(1,len(nums)):

            if nums[left]+k >= nums[pos]-k:
                ans = max(ans,pos-left+1)

            while left<pos and nums[left]+k<nums[pos]-k:
                left+=1

        return ans


            



        