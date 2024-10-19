class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        result = 0
        start = 0
        for end in range(len(nums)):
            temp = start
            while(temp<end):
                if nums[temp] & nums[end] !=0:
                    start = temp+1

                temp+=1
            result = max(result, end-start+1)


        return result