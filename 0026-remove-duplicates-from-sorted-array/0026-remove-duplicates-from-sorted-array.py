class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) ==1:
            return 1

        pos = 0
        for i , val in enumerate(nums):
            if i>0 :

                if nums[pos]<val:
                    pos+=1
                    nums[pos] = val


        return pos+1

    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) ==1:
            return 1

        left =0
        for right in range(len(nums)):
            if nums[right]>nums[left]:
                left+=1
                nums[left]= nums[right]

        return left+1
                   
              

        