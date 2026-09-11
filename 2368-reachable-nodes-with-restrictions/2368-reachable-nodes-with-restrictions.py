class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        adj = graph = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n
        for node in restricted:
            visited[node] = True

        queue= []
        queue.append(0)
        visited[0] = True
        count = 1
        while queue:
            node  = queue.pop(0)
            
            for child in adj[node]:

                if not  visited[child] :
                    queue.append(child)
                    visited[child] = 1
                    count+=1
        return count

class Solutionn:
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
        
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # using union and find approach

        parents = [i for i in range(n)]
        size = [0 for i in range(n) ]

        def find(node):
            if parents[node]!= node:
                parents[node] = find(parents[node])

            return parents[node]

        for a,b in edges:
            if a in restricted or b in restricted:
                continue 
            p1 = find(a)
            p2 = find(b)
            if p1!=p2:

                if p1 == 0 and not p2 in restricted:
                    parents[p2] = p1
                    size[p1]+=size[p2]+1
                elif p2 ==0 and not p1 in restricted:
                    parents[p1] =p2
                    size[p2]+=size[p1]+1

                else:
                    if size[p1]>size[p2]:
                        parents[p2] = p1
                        size[p1]+=size[p2]+1
                    else:
                        parents[p1] =p2
                        size[p2]+=size[p1]+1
        return size[0]+1

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = [0 for _ in range(n)]
        restricted = set(restricted)

        def dfs(node):

            if visited[node] ==1 or node in restricted:
                return


            visited[node] =1

            for neigh in adj[node]:

                if visited[neigh] or  not neigh in restricted:

                    dfs(neigh)
                    print(neigh)

            return

        dfs(0)
        c=0
        print(visited)
        for node in visited:
            if node == 1:
                c+=1

        return c

