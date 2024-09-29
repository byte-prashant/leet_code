class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # brute force

        peak =  -1

        for index in range(1, len(nums)-1):
            if nums[index]> nums[index-1] and nums[index]>nums[index+1]:
                return index

        if len(nums) ==1:
            return 0
        elif nums[0]>nums[1]:
            return 0
        else:
            return len(nums)-1



        