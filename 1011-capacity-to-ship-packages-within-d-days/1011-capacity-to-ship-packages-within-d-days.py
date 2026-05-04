class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def no_of_days(max_weight):
            count=0
            remaining_weight = max_weight
            for weight in weights:
                if not remaining_weight-weight>0:
                    count+=1
                    remaining_weight = max_weight
                remaining_weight -= weight
            # if remaining_weight>0:
            #     count+=1
            
            
            return count

        def no_of_days(max_weight):
            days =1
            curr =0
            for w in weights:
                if curr+w>max_weight:
                    days+=1
                    curr =0
                curr+=w
            return days

        left = ans = max(weights)
        right = sum(weights)

        while left<right:
            mid = (left+right)//2

            ans_days = no_of_days(mid)
            

            if ans_days<=days:  # can ship, try with smaller one
                ans = mid
                right = mid
            else:              # can not ship try with larger one
                left = mid+1

            #print(ans_days,left,right,mid)

        return left