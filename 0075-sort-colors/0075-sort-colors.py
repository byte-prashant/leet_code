class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos=0
        left=0
        right = len(nums)-1
        while pos<=right:
            if nums[pos]==0:
                nums[pos],nums[left] = nums[left],nums[pos]
                left+=1
                
                pos+=1
            elif nums[pos]==2:
                nums[right],nums[pos] = nums[pos],nums[right]
                right-=1
            else:
                pos+=1

        return nums

        