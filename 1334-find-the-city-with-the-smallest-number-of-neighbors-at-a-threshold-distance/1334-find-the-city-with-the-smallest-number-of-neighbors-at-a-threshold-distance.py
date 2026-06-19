class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        INF = float("inf")

        distance = [[INF]*n for _ in range(n)]
        # as this is undirected graph make it directed one

        # add direct edges
        for u,v,w in edges:
            distance[u][v] = w
            distance[v][u] = w

        for via in range(n):
            for src in range(n):
                for dst in range(n):
                    if distance[src][via]!=INF and distance[via][dst]!=INF:

                        distance[src][dst] = min(distance[src][dst],distance[src][via]+distance[via][dst])

        city_ans,ans_count = None,INF
        print(distance)
        for city in range(n):
            count = 0
            for neigh,dis in enumerate(distance[city]):
                if city!= neigh and dis<=distanceThreshold:
                    count+=1
            print(count)
            if ans_count>=count:
                ans_count = count
                city_ans = city

        return city_ans

            


        