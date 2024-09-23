class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        if len(nums)==2:
            return min(nums)

        minnimum = float("+inf")
        l = 0
        r = len(nums)-1
        mid =0 
        while(l<r):
            mid = l+(r-l)//2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
            print(mid)

        return minnimum
        