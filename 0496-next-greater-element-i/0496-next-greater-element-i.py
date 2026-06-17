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
        



    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import deque
        freq_nums1 = {key:val for val,key in enumerate(nums1)}
        stack = deque()
        ans = nums1[:]
        #print(ans,len(ans))
        for pos in range(len(nums2)-1,-1,-1):
            
            while stack and stack[-1]< nums2[pos]:
                stack.pop()
            
            if nums2[pos] in freq_nums1:
                index = freq_nums1[nums2[pos]]
                #print(index)
                if stack:
                    ans[index] = stack[-1]
                else:
                    ans[index] =-1
                
                    
            stack.append(nums2[pos])
        return ans

