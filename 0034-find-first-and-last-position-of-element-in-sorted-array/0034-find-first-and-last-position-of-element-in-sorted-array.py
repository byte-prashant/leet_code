# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:

#         left = 0
#         right = len(nums)-1
#         index = -1
#         while(left<=right):
#             mid = left + (right-left)//2

#             if nums[mid] == target:
#                 index = mid

#             if nums[mid]<target:
#                 left = mid+1
#             else:
#                 right = mid-1
      
#         lo = hi = index
#         if index == -1:
#             return [-1,-1]
#         while(lo>0 and nums[lo-1]== target ):
#                 lo = lo-1
        
#         while(hi+1<len(nums) and nums[hi+1] == target ):
#                 hi = hi+1

#         return [lo,hi] 


# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         low =0 
#         high = len(nums)-1
#         index =  -1
#         while low<=high:
#             mid = low + (high-low)//2

#             if target == nums[mid]:
#                 index = mid

#             if  target<nums[mid]:
#                 high = mid-1
#             else:
#                 low = mid+1

            

#         low = high =index

#         if index == -1:
#             return  [-1,-1]


#         while low>=0  and  low-1 >=0 and nums[low-1] == target:
#                 low-=1
            

#         while high< len(nums) and  high+1< len(nums) and nums[high+1] == target:
#                 high+=1
            

#         return [low,high]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftmost():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def rightmost():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [leftmost(), rightmost()]