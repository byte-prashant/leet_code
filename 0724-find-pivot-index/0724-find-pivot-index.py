class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for index in range(len(nums)):
            if left_sum == total_sum-(left_sum+nums[index]):
                return index
            left_sum = left_sum+nums[index]
        return -1


        