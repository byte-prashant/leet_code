class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:

        ans = 0
        for pos, height in enumerate(heights):

            if pos ==0:
                continue

            if height < heights[pos-1]:
                continue

            if height-heights[pos-1]<=bricks:

                bricks-=height-heights[pos-1]

            elif ladders>0:
                ladders-=1

            else:
                
                break
            ans=pos

        while ans+1 <len(heights):

            if heights[ans]>heights[ans+1]:
                ans+=1
            else:
                break
        return ans
            

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        pq = []
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if len(pq) < ladders:
                    heappush(pq, diff)
                else:
                    if not pq or pq[0] >= diff:
                        bricks -= diff
                    else:
                        poll = heappop(pq)
                        heappush(pq, diff)
                        bricks -= poll
                    if bricks < 0:
                        return i
        return n-1

        

