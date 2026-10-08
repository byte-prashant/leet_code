class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:

        stack = []

        minsum = maxsum = 0

        for right in range(len(nums)+1):

            while stack and (right== len(nums) or nums[stack[-1]]>nums[right]):

                mid = stack.pop()
                left =  stack[-1] if stack else -1
                minsum+=  nums[mid]*(mid-left)*(right-mid)

            stack.append(right)

        stack = []
        for right in range(len(nums)+1):

            while stack and (right == len(nums) or nums[stack[-1]]<nums[right]):

                mid = stack.pop()
                left =  stack[-1] if stack else -1
                maxsum+=  nums[mid]*(mid-left)*(right-mid)

            stack.append(right)


        return maxsum-minsum


        








        