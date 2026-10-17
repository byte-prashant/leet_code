class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:


        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]
        n = len(nums)
        for index,num in enumerate(nums):

            if index ==0:
                continue
            prefix_sum[index] = prefix_sum[index-1]+num

        ans = [float("+inf")]
        def sol(pos,k,max_sum):

           

            if k==1:
                ans[0] = min(
                    ans[0],
                    max(max_sum, prefix_sum[n - 1] - prefix_sum[pos])
                )

                return

            for split_index in range(pos+1,n-k+1):
                new_max_sum = max(max_sum,prefix_sum[split_index]-prefix_sum[pos])

                sol(split_index,k-1,new_max_sum)

            return
        if k == 1:
            return prefix_sum[n - 1]

        for pos in range(len(nums)-k+1):

            sol(pos,k-1, prefix_sum[pos])

        return ans[0]










from functools import lru_cache

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]

        for index in range(1, n):
            prefix_sum[index] = prefix_sum[index - 1] + nums[index]

        @lru_cache(None)
        def sol(pos, k):

            if k == 1:
                return prefix_sum[n - 1] - (
                    prefix_sum[pos - 1] if pos > 0 else 0
                )

            ans = float("inf")

            for split_index in range(pos, n - k + 1):

                current_sum = prefix_sum[split_index] - (
                    prefix_sum[pos - 1] if pos > 0 else 0
                )

                remaining_sum = sol(split_index + 1, k - 1)

                ans = min(
                    ans,
                    max(current_sum, remaining_sum)
                )

            return ans

        return sol(0, k)





        