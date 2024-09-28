class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left =0 
        right = len(nums)-1
        while(left<=right):
            print(left)
            mid = left+(right-left)//2
           
            if nums[mid]==target:
                return mid

            elif nums[mid]<target:
                left = mid+1

            else:
                
                right = mid-1
            print(left, right,"---")
        return left

        