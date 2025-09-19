class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_product = [1]*len(nums)
        ans = [1]*len(nums)
        for index in range(1,len(nums)):
           
            left_product[index] = left_product[index-1]*nums[index-1]
        right =1
       
        ans[len(nums)-1]= left_product[len(nums)-1]

        for index in range(len(nums)-2,-1,-1):
            
            right = nums[index+1]*right
            ans[index] = left_product[index]*right

        return ans

            
            

        

        