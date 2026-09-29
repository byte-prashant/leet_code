class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:

        stack= []
        arr.append(0)
        ans = 0
        stack = [-1]

        for cur_index , num in enumerate(arr):

            while stack and arr[stack[-1]]>num:
                index = stack.pop()

                left = index- stack[-1]

                right = cur_index-index


                ans+= left*right*arr[index]

            stack.append(cur_index)

        return ans%(10**9+7)





        