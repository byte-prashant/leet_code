class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        ans = []
        left = 0
        right = 0
        while  left+1 <len(nums) and nums[left+1]<0:
            left+=1
        right=left+1

        #print(left,right)
        while left>=0 and right<len(nums):
            if nums[left]*nums[left]>nums[right]*nums[right]:
                ans.append(nums[right]*nums[right])
                right+=1
               

            else:
                ans.append(nums[left]*nums[left])
                left-=1

        #print(right)
        while right<len(nums):
            ans.append(nums[right]*nums[right])
            right+=1

        
        while left>=0:
            ans.append(nums[left]*nums[left])
            left-=1

        return ans




        