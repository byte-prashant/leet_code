class Solution:
    from decimal import Decimal
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        time = []
        for i in range(len(dist)):
            time.append((dist[i]/speed[i]))

        time = list(sorted(time))
        print(time)
        count = 0
        ans = 0
        for i in range(len(dist)):

           
            
            if count<time[i]:
                ans+=1
            else:
                break


            count+=1

            
        return ans





