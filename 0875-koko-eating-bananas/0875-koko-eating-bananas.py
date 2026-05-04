class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)>h:
            return -1

        if len(piles)==h:
            return max(piles)

        total_banas = sum(piles)
        minimum_banas = left = 1
        right = max(piles)
        ans = right
        while left<=right:
            mid = minimum_banas = (left+right)//2
            #hours = total_banas//minimum_banas
            #hours = sum((p + mid - 1) // mid for p in piles)
            hours = sum(math.ceil(p / mid) for p in piles)

            
            if hours<=h:
                ans = mid
                right=mid-1
            else:
                left= mid+1
        return ans

