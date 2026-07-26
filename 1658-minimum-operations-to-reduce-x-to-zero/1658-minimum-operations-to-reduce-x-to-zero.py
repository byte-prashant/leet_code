class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:

       
        # trying with circular wrap around
        # minimum length subarray with summ == x
        from math import inf

        def min_circular_subarray(nums, target):
            n = len(nums)
            arr = nums + nums

            left = 0
            curr = 0
            ans = inf

            for right in range(2 * n):
                curr += arr[right]

                while left < n and (
                    curr > target or
                    right - left + 1 > n
                ):
                    curr -= arr[left]
                    left += 1

                if left >= n:
                    break

                if curr == target:
                    ans = min(ans, right - left + 1)

            return -1 if ans == inf else ans

        return min_circular_subarray(nums,x)

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        target = sum(nums) - x
        if target < 0:
            return -1

        if target == 0:
            return len(nums)
        left = current_sum = 0

        max_len = 0

        for right,val in enumerate(nums):
            current_sum+=nums[right]


            while left<=right and current_sum>target:
                current_sum-=nums[left]
                left+=1
                

            
            if target == current_sum:
                max_len = max(max_len,right-left+1)

        
        
        return len(nums) - max_len if max_len else -1


    
