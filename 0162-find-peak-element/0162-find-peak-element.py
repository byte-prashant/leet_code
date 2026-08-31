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


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left<right:

            mid = left+(right-left)//2

            if nums[mid]<nums[mid+1]:

                left=mid+1

            else:
                # it should  mid onlye
                # as we are on down hill
                # and  mid could be an ans
                right = mid
        return left
        