class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = [float("-inf")]
        def recur(pos, summ):
            
            max_sum[0] = max(max_sum[0], summ)
            if pos == len(nums):
                return

            if summ == float("-inf"):
                summ = 0

            recur(pos+1,summ+nums[pos])

            return

        for i in range(0, len(nums)):
            recur(i, float("-inf"), "")

        return max_sum[0]



    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                max_sum = max(max_sum, sum(nums[i:j+1]))

        
        return max_sum


    

    def maxSubArray(self, nums: List[int]) -> int:

        summ = 0
        maxx = float("-inf")
        for ele in nums:
            summ  = max(ele,summ+ele)
            maxx = max(summ, maxx)
        
        return maxx

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        for i in range(len(nums)):
            # for all sub arrays ending at index i

            # following is the repetitive task
            # follwogn give  subarray having max_sum ending at position i
            for j in range(0, i+1):
                summ = 0
                sub_arr =""
                for k in range(j, i+1):
                    sub_arr+=str(k)
                    summ+=nums[k]
                    max_sum = max(max_sum,summ )
                    #print(max_sum)

            #print(max_sum)

        
        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        dp = [0]*len(nums)
        for i in range(len(nums)):
            # for all sub arrays ending at index i
            curr_max = float("-inf")
            if i ==0:
                curr_max = nums[0]
            else:
                # we are only using previous value of dp
                curr_max = max(nums[i], dp[i-1]+nums[i])

            dp[i] = curr_max
            max_sum = max(max_sum, curr_max)

            #print(max_sum)

        
        return max_sum


    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(float("-inf"), nums[0])
        
        dp = nums[0]
        for i in range(1,len(nums)):
            # for all sub arrays ending at index i
            
            curr_max = max(nums[i], dp+nums[i])

            dp = curr_max
            max_sum = max(max_sum, curr_max)

            #print(max_sum)

        
        return max_sum


   

   




        