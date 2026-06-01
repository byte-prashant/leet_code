class Solution:
    def maxArea(self, height: List[int]) -> int:
        #min(highti,hightj)*(indexj-indexi)

        low, high = 0, len(height)-1
        max_cap = 0
        while(low<high):
            print(low,high)
            max_cap = max(min(height[low],height[high])*(high-low), max_cap)
            if height[low]<=height[high]:
                low+=1
            else:
                high-=1
        return max_cap

        