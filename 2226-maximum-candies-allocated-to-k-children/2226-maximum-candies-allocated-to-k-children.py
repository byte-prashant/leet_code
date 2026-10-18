class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:

        def is_valid(candies_per_child,children):

            for candies_per_pile in candies:

                no_of_child = candies_per_pile//candies_per_child
                
                children-=no_of_child

                if children<=0:
                    return True

            if children <=0:
                return True

            return False

        
        if sum(candies)<k:
            return 0


        left =  1
        right = max(candies)
        ans = 0
        while left <=right:

            mid = (left + right)//2


            if is_valid(mid,k):

                left = mid+1
                ans = mid

            else:
                right = mid-1


        return ans



                





        
        