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

        