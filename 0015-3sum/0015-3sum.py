class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            summ =0 
            if i>0 and  nums[i]==nums[i-1]:
                continue
            while left<right:
                summ=nums[left]
                summ+=nums[right]
                summ+= nums[i]

                if summ>0:
                    right-=1
                elif summ<0:
                    left+=1
                elif summ ==0 :
                    ans.append((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
        return ans


        