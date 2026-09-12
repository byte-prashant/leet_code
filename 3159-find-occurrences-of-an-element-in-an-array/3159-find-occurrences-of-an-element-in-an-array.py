class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        left =0
        for right, val in enumerate(nums):
            if val ==x:
                nums[left] = right
                left+=1

        for pos , val in enumerate(queries):
            if val-1<left:
                queries[pos] = nums[val-1]
            else:
                queries[pos] = -1
        return queries


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:

        dp = {}
        ocu = 0
        for index, num in enumerate(nums):
            if num == x:
                ocu+=1
                dp[ocu] =index
        
        ans = []
        for q in queries:
            if q in dp:
                ans.append(dp[q])
            else:
                ans.append(-1)

        return ans