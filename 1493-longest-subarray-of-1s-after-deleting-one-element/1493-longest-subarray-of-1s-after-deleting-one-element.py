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

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        zero_count =0
        
        longest_window = float("-inf")
        left=0
        for right in range(len(nums)):
            zero_count+= 1 if nums[right] ==0 else 0

            while zero_count>1:
                zero_count-= 1 if nums[left] ==0 else 0

                left+=1

            longest_window = max(longest_window,right-left)

        return longest_window
