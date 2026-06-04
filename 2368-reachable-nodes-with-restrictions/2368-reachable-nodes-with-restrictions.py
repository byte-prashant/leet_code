class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        from collections import defaultdict
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)


        queue= [0]
        visited = {0:1}
        count = 1
        while queue:
            node  = queue.pop(0)
            
            for child in adj[node]:

                if not child  in restricted and not child in visited :
                    queue.append(child)
                    visited[child] = 1
                    count+=1
        return count
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        for node in restricted:
            visited[node] = True

        queue = deque()
        queue.append(0)
        visited[0] = True

        while queue:
            curr = queue.pop()
            for child in graph[curr]:
                if not visited[child]:
                    queue.append(child)
                    visited[child] = True
        
        return sum(visited) - len(restricted)
        