class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:

        stack = []
        stack.append(len(heights)-1)
        ans = [0 for _ in range(len(heights))]

        for pos in range(len(heights)-2,-1,-1):
            lower_height_people_in_front = 0
            while stack and heights[stack[-1]]<heights[pos]:
                stack.pop()    
                lower_height_people_in_front+=1
            ans[pos] = lower_height_people_in_front

            if stack:
                ans[pos]+=1
            stack.append(pos)

        return ans