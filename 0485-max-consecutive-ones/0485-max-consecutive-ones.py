class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        max_1 = 0
        for num in nums:
            if num == 0:
                max_1 = max(max_1,c)
                c = 0
            else:
                c+=1
        max_1 = max(max_1,c)
        return max_1

        
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)
        ans = 0
        c = 0
        for  right in range(len(nums)):

            if nums[right] == 0:
                ans = max(ans,c)
                left = right
                c = 0
            else:
                c +=1

        ans = max(ans,c)
        return ans