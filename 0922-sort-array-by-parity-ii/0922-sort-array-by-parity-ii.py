class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        odd = 1
        even = 0
        ans = [0]*len(nums)

        for num in nums:
            if num %2 ==0:
                ans[even] =num
                even+=2
            else:
                ans[odd] = num
                odd+=2
        return ans

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        odd =1
        even = 0
        pos = 0
        
        while even<len(nums):

            if not nums[even]&1:
                even+=2
            elif nums[odd]&1:
                odd+=2

            else:
                nums[even],nums[odd] = nums[odd], nums[even]
                even+=2
                odd+=2
            

        return nums


        