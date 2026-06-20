class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict

        adj = defaultdict(list)
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)


        visited =[False]*n

        def dfs(node):

            visited[node] = True
            ans = 0
            for neigh in adj[node]:

                if not visited[neigh]:
                    ans = max(ans,dfs(neigh)+1)

            return ans
        height = []
        for i in range(n):
            visited =[False]*n
            height.append((dfs(i),i))

        height.sort(key = lambda x: x[0])

        print(height)

        ans = [height[0]]
        
        for h in height[1:]:
            if ans[-1][0] == h[0]:
                ans.append(h)
            else:
                break

        return [ ele[1] for ele in ans]




# three wil only be two possible roots of minimum height
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict,deque

        adj = defaultdict(list)
        degree = [0]*n
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
            degree[src]+=1
            degree[dst]+=1

        if n==1:
            return [0]
        queue = deque()
        for  node, indeg in enumerate(degree):
            if indeg ==1:
                queue.append(node)


        nodes = n
        while nodes>2:
            level_elems = len(queue)
            nodes -= level_elems

            for _ in range(level_elems):

                elem = queue.popleft()

                for neigh in adj[elem]:
                    degree[neigh]-=1
                    if degree[neigh] ==1:
                        queue.append(neigh)


        return list(queue)







        