class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        def sol():
            left = 0
            right = 0
            summ =  [0]*len(nums)
            
            maxx = 0
        
            dp = {}
            while(right<len(nums)):
                if right==0:
                    summ[right]  = nums[0]
                else:
                    summ[right] = summ[right-1] + nums[right]

                if not  nums[right] in dp or dp[nums[right]]<left:
                    dp[nums[right]]  = right
                    if right-left==k-1:
                        maxx = max(maxx, summ[right]-summ[right-k+1]+nums[right-k+1])    
                        left+=1
                else:
                    left = dp[nums[right]]+1
                    dp[nums[right]] = right
                    
                
                right+=1


            return maxx


        def sol2(k):
            left = 0
            right = 0
            summ =  0
            
            maxx = 0
        
            last_seen = {}
            while(right<len(nums)):
                

                if nums[right] in last_seen and last_seen[nums[right]]>=left:
                    left = last_seen[nums[right]]+1
                    summ =0
                    # we can use prefix here
                    for l in range(left, right):
                        summ+=nums[l]
                   
                summ+= nums[right]
                last_seen[nums[right]] = right
                if right-left+1 ==k:

                    maxx = max(maxx, summ)
                    summ-=nums[left]
                    left+=1
                
                right+=1
            return maxx

# as we require sum of window lenth k, we can use one varible to store that

        def sol1(k):
            n = len(nums)
            if k > n:
                return 0
            
            max_sum = 0
            current_sum = 0
            window = set()
            start = 0
            
            for end in range(n):
                # If the element is already in the set, move the start pointer
                while nums[end] in window:
                    window.remove(nums[start])
                    current_sum -= nums[start]
                    start += 1
                
                # Add the current element to the window and current sum
                window.add(nums[end])
                current_sum += nums[end]
                
                # Check if the window size is k
                if end - start + 1 == k:
                    max_sum = max(max_sum, current_sum)
                    # Prepare to slide the window by removing the start element
                    window.remove(nums[start])
                    current_sum -= nums[start]
                    start += 1
            
            return max_sum

        def sol3(k):

            res, cur, pos, left = 0, 0, [-1] * 100001, -1
            for i in range(0, len(nums)):
                cur += nums[i]
                if i >= k:
                    cur -= nums[i - k]
                left = max(left, pos[nums[i]])
                if i - left >= k:
                    res = max(cur, res)
                pos[nums[i]] = i
            return res


        return sol3(k)

        




        

        