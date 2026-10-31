class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:


        chnunks = 0
        stack = []

        for pos in range(len(arr)):

            if not stack or stack[-1]<=arr[pos]:

                stack.append(arr[pos])
                continue

            
            ele = arr[pos]
            while stack and  stack[-1]>arr[pos]:
                ele = max(ele,stack.pop())

            stack.append(ele)

        return len(stack)





        