class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        import heapq
        from collections import defaultdict
        adj = defaultdict(list)
        for flight in flights:
            _src,_dst,price = flight
            adj[_src].append((price,_dst))

        stops_seen = [float('inf')] * n

        pq = [(0,src,0)]
        #visited[src] = True
        ans = [float("inf"),float("inf"),]
        while pq:
            price, _src, stops = heapq.heappop(pq)
            if _src == dst:
                if stops<=k:
                    
                    if ans[0]>price:
                        ans = [price,stops]
                      

                    elif ans[0]==price:
                        if ans[1]<stops:
                            ans = [price,stops]
                continue

            if stops>k:
                continue

            if stops>=stops_seen[_src]:
                continue

            
            stops_seen[_src] = stops

            for neigh in adj[_src]:
                    _price,_dst = neigh
              
                    
                    _stops = stops
                    if  _dst != dst:
                       
                        _stops = stops+1
                   
                    if _stops<=k:
                        heapq.heappush(pq,(price+_price,_dst,_stops))

        return ans[0] if ans[0]!= float("inf") else -1
        
        

import heapq
from collections import defaultdict

class Solutionn:
    def findCheapestPrice(self, n, flights, src, dst, k):

        adj = defaultdict(list)

        for u, v, price in flights:
            adj[u].append((v, price))

        pq = [(0, src, 0)]

        stops_seen = [float('inf')] * n

        while pq:

            cost, node, stops = heapq.heappop(pq)

            if node == dst:
                return cost

            if stops > k:
                continue

            if stops >= stops_seen[node]:
                continue

            stops_seen[node] = stops

            for neigh, wt in adj[node]:
                heapq.heappush(
                    pq,
                    (cost + wt, neigh, stops + 1)
                )

        return -1

        

        