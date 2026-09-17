class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        heights.append(0)

        stack = []
        ans = 0
        # monotonic stack
        # finds the boudary for each element, left and right

        for i , height in enumerate(heights):
            # for stack top element right boundary is height
            # left boudary is last element of stack
            # 1,2,3,4,5 , stack contains continuous increasing elements
            while stack and height < heights[stack[-1]]:
                
                pop_index  = stack.pop()

                pop_height = heights[pop_index]

                if stack:
                    width =  i - stack[-1] -1
                    # -1 ,we will not include ith element as it is smallest

                else:
                    width = i
                    # means all elements of it lefts are smaller ones

                ans = max(ans , pop_height*width )

            stack.append(i)

        return ans



