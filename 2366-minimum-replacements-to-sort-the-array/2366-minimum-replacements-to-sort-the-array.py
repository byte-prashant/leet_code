class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        right_min = nums[len(nums)-1]
        no_of_operations = 0
        for right in range(len(nums)-2,-1,-1):

            if nums[right]<=right_min:
                right_min = nums[right]
                continue

            mul = nums[right]//right_min
            remainder = nums[right]%right_min

            if remainder>0:
                no_of_operations+=mul
               # right_min = remainder
               # caluclate correct minimum possible element
                right_min = nums[right]//(mul+1)

            else:
                no_of_operations+=mul-1


        return no_of_operations









        