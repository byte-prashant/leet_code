class Solution:
    def sortPermutation(self, nums: List[int]) -> int:

        res = -1
        for index, val in enumerate(nums):

            if val != index:
                res &= val

        
        return 0 if res ==  -1 else res
        