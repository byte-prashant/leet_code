class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
            i = 0
            k=1
            for j in range(len(nums)):
                k -= 1 - nums[j]
                if k < 0:
                    k += 1 - nums[i]
                    i += 1
            return j - i

