class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        from collections import defaultdict
        import heapq
        no_node = n
        adj_list = defaultdict(list)
        for src,dst,time in times:
    
            adj_list[src].append((dst,time))

        
        queue = [(0,k)]
        no_node-=1
        heapq.heapify(queue)
        min_req_time = 0
        visited = [float("inf")] * (n + 1)
        visited[k] =0
        while queue :

            time,src = heapq.heappop(queue)

            if time>visited[src]:
                continue

            for neigh, dst_time in adj_list[src]:

              
                if dst_time+time <visited[neigh]:
                    visited[neigh] = dst_time+time
                    heapq.heappush(queue,( dst_time+time,neigh))

        
        min_req_time = max(visited[1:])

        return   min_req_time if min_req_time!= float("inf") else -1  










        
        

        
        