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
        