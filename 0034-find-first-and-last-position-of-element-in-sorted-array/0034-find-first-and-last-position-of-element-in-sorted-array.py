class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums)-1
        index = -1
        while(left<=right):
            mid = left + (right-left)//2

            if nums[mid] == target:
                index = mid

            if nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
      
        lo = hi = index
        if index == -1:
            return [-1,-1]
        while(lo>0 and nums[lo-1]== target ):
                lo = lo-1
        
        while(hi+1<len(nums) and nums[hi+1] == target ):
                hi = hi+1

        return [lo,hi] 


        