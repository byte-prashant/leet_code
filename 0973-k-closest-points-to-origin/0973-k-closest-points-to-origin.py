class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        points_dist = []
        import math
        for point in points:
            x,y = point
            dist = math.sqrt(x*x+y*y)
            points_dist.append((dist,(x,y)))

        points_dist.sort(key=lambda x: x[0])

        return [point for dis,point in points_dist[:k]]
        