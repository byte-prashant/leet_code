class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            zeroes = 0
            ones = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zeroes += 1
                else:
                    ones += 1
                if zeroes == ones:
                    ans = max(ans, j - i + 1)
        return ans


    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        
        target = 0
        prefix_sum = -1 if not nums[0] else 1
        hash_map = {prefix_sum:0}
        for i in range(1,len(nums)):
            
            if nums[i] == 0:
                prefix_sum -=1
            else:
                prefix_sum+=1

            if prefix_sum == target:
                ans = max(ans, i+1)

            if prefix_sum - target in hash_map:

                ans = max(ans, i-hash_map[prefix_sum - target])

            else:
                hash_map[prefix_sum - target] = i

        print(hash_map)
        return ans

        