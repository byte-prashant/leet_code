class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        from collections import defaultdict

        adj = defaultdict(list)

        for src,dst in connections:
            adj[src].append(dst)
            #addj[dst].append(src)

        print(adj)
        timer = 0
        low_time = [-1]*n
        tin = [-1]*n
        ans = []
        low_time[0] =1
        def dfs(node, timer):
            timer+=1
            tin[node] = timer
            if not adj[node]:
                low_time[node] = timer

            for neigh in adj[node]:
                if tin[neigh]>-1:
                    low_time[node] = tin[neigh]
                else:
                    dfs(neigh,timer)
                    print(low_time,node)
                    low_time[node] = min(low_time[neigh],low_time[node])
                    if low_time[node]!= low_time[neigh]:
                        ans.append([node,neigh])
          

        dfs(0,timer)
        print(low_time,tin)
        return ans

class Solution:
    def criticalConnections(self, n, connections):

        from collections import defaultdict

        adj = defaultdict(list)

        for src, dst in connections:
            adj[src].append(dst)
            adj[dst].append(src)

        tin = [-1] * n
        low = [-1] * n
        timer = 0
        ans = []

        def dfs(node, parent):
            nonlocal timer

            tin[node] = low[node] = timer
            timer += 1

            for neigh in adj[node]:

                if neigh == parent:
                    continue

                if tin[neigh] != -1:
                    # back edge
                    low[node] = min(low[node], tin[neigh])

                else:
                    dfs(neigh, node)

                    low[node] = min(low[node], low[neigh])

                    if low[neigh] > tin[node]:
                        ans.append([node, neigh])

        dfs(0, -1)

        return ans


        