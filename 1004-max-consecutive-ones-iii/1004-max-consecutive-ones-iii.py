class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        def sol():
            left = 0
            zero_count = 0
            maxx = 0

            for right in range(len(nums)):
                if nums[right]==0:
                    if zero_count == k:
                        if nums[left]==1:
                            while(nums[left]!=0):
                                left+=1
                        zero_count -=1
                        left+=1 # removed one zero count
                    
                    zero_count+=1
                    print(left,right,zero_count)

                maxx = max(maxx, right-left+1)
            return maxx

        def sol(k):
            left = 0
            for right in range(len(nums)):
                # If we included a zero in the window we reduce the value of k.
                # Since k is the maximum zeros allowed in a window.
                k -= 1 - nums[right]
                # A negative k denotes we have consumed all allowed flips and window has
                # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
                if k < 0:
                    # If the left element to be thrown out is zero we increase k.
                    k += 1 - nums[left]
                    left += 1
            return right - left + 1

        return sol(k)


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j]
            while k < 0:

                k += 1-nums[i]
                i+=1

            ans = max(ans, j-i+1)

        return ans


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        from bisect import bisect_left
        ans = 0
        left = 0
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + (num == 0))
       # print(prefix)
        for right in range(len(prefix)):
            target = prefix[right]-k

            # prefix[j]-prefix[i]<=k
            # prefix[i]>=prefix[j]-k
            left = bisect_left(prefix, target)
            ans = max(ans, right - left)

        return ans


        
            
                



                    
            