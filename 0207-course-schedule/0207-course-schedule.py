class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        def dfs(node,stack,visited):
            # to detect cycle
            if stack[node]:
                return True
            # to detect nodes visted, DP
            # we have successsfully visited this node
            # no need to
            if visited[node]:
                return False

            visited[node] = True
            stack[node] = True
            for n in adj[node]:
                if dfs(n,stack,visited):
                    return True
            stack[node] = False
            return False

        
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[0]].append(prerequisite[1])


        visited = [False] * numCourses
        #print(adj)
        for i in range(numCourses):
            print(i)
            instack = [False] * numCourses
            if dfs(i,instack,visited):
                return False
            #print("sfd",instack)
        return True

        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        indegree = [0]*numCourses
        for start,end in prerequisites:
            indegree[end]+=1

            if start in adj:
                adj[start].append(end)
            else:
                 adj[start] = [end]


        queue = []
        for node, degree in enumerate(indegree):
            if degree == 0:
                queue.append(node)

        if not queue:
            return False

        #print(queue,indegree,adj)
        ans =  []
        while queue:

            node = queue.pop(0)

            ans.append(node)
            
            if node in adj:
                for neighbour in adj[node]:
                    indegree[neighbour]-=1

                    if indegree[neighbour] == 0:
                        queue.append(neighbour)

        return  len(ans) == numCourses



        

        

        








        
        