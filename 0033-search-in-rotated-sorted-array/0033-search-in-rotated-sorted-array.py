class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def find_min(nums):
            left = 0 
            right = len(nums)-1

            while(left<right):
                mid = left + (right-left)//2

                if nums[mid]>nums[right]:
                    left = mid+1
                else:
                    right = mid

            return left

        left = 0 
        right = len(nums)-1

        mid_index = find_min(nums)
        
        if nums[mid_index] == target:
            
            return mid_index

        
        lo,hi = 0,0
        if nums[mid_index]< target and target<=nums[right]:
            lo = mid_index+1
            hi = right
        else:
            lo = 0
            hi = mid_index-1


        


        while(lo<=hi):

            mid = lo + (hi-lo)//2

            if nums[mid]==target:
                return mid

            elif nums[mid]<target:
                lo= mid+1

            else:
                hi = mid-1

        return -1

        

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2

            # Case 1: find target
            if nums[mid] == target:
                return mid

            # Case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Case 3: subarray on mid's right is sorted.
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1