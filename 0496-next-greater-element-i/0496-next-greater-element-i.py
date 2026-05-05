class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        dp = {}
        stack= [-1]
        for num in nums2[::-1]:
            if num <stack[-1]:
                dp[num] = stack[-1]
                stack.append(num)
            else:
                while stack and len(stack)>1 and stack[-1]<=num:
                    stack.pop()

                dp[num] = stack[-1]
                stack.append(num)
        #print(dp)
        ans = []
        for pos , num in enumerate(nums1):
            if num in dp:
                ans.append( dp[num])
            else:
                ans.append(-1)

        return ans
        