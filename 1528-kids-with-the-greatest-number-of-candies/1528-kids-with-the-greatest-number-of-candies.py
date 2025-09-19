class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        gt_can = max(candies)
        result = [False]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=gt_can:
                result[i] = True

        return result