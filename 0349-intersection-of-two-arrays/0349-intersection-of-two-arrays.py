class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dp = {}

        for num in nums1:
            dp[num] = 1

        ans = []
        for num in nums2:
            if num in dp:
                ans.append(num)

        return list(set(ans))