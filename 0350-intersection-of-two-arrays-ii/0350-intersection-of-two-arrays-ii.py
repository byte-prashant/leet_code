class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dp = defaultdict(int)
        for num in nums1:
            dp[num]+=1
        ans = []
        for num in nums2:
            if num in dp and dp[num]>0:
                ans.append(num)
                dp[num]-=1

        return ans
            
        