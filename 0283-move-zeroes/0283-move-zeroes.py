class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # not maintaning the relative order
        left = 0
        right = len(nums)-1

        while(left<right):

            if nums[left] == 0:

                if nums[right]!=0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left+=1
                
                right-=1

            else:
                left+=1

        return nums


    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # not maintaning the relative order
        left = 0
        right = 1

        while(right<len(nums)):
            
            if nums[right]!=0:

                if nums[left]==0:
                    nums[left], nums[right] = nums[right], nums[left]
                    right+=1
                if right == left:
                    right+=1

                left+=1
            else:
                right+=1

        return nums


    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # not maintaning the relative order
        left = 0
        for right in range(len(nums)):

            if nums[right]!=0 and nums[left]==0:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left]!=0:
                left+=1


        return nums




        