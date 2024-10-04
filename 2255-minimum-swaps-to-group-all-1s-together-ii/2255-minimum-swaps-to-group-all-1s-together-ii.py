class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        window_len = 0

        for num in nums:
            if num:
                window_len+=1
        zero_count = 0
        left = 0
        right = 0
        new_num = nums+nums[0:window_len]

        while(right<window_len):
            if nums[right]==0:
                zero_count+=1

            right+=1

        req_swaps = zero_count
        checked_cycle = False
        print(new_num,left,right)
        while(right<len(new_num)):

            
            

            if new_num[right]==0:
                zero_count+=1
    
            if new_num[left] == 0:
                zero_count-=1
                
            print(left+1, right,zero_count)
            req_swaps = min(zero_count,req_swaps)

           
            right+=1
           
            left+=1

        return req_swaps



        