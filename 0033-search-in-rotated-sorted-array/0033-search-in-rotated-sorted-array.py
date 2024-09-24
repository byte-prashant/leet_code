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
        print("mid ",mid_index, nums[mid_index] == target, nums[mid_index] ,target)
        if nums[mid_index] == target:
            print("found mid")
            return mid_index
        lo,hi = 0,0
        if nums[mid_index]< target and target<=nums[right]:
            lo = mid_index+1
            hi = right
        else:
            lo = 0
            hi = mid_index-1


        print(lo, hi)


        while(lo<=hi):

            mid = lo + (hi-lo)//2

            if nums[mid]==target:
                return mid

            elif nums[mid]<target:
                lo= mid+1

            else:
                hi = mid-1

        return -1

        

        