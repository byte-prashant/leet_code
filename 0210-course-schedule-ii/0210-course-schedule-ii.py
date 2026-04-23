class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node,stack,visited, order):
            if stack[node]:
                return True

            if visited[node]:
                return False

            visited[node] = True
            stack[node] = True
            for n in adj[node]:
                if dfs(n,stack,visited,order):
                    return True
            stack[node] = False
            order.append(node)
            return False

        
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[0]].append(prerequisite[1])


        visited = [False] * numCourses
        order = []
        for i in range(numCourses):
            
            instack = [False] * numCourses
            if dfs(i,instack,visited,order):
                return []
            
            #print("sfd",instack)
        return order

    def findOrder(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:

        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = deque(
            [k for k in range(numCourses) if k not in indegree]
        )

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return (
            topological_sorted_order
            if len(topological_sorted_order) == numCourses
            else []
        )

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0]*numCourses
        for source,destination  in prerequisites:
            adj[destination].append(source)
            indegree[source]+=1
        topological = []

        queue = deque(node for node, degree in enumerate(indegree) if degree == 0 )
        if not queue:
            return []
        while queue:
            node = queue.popleft()
            topological.append(node)
            if node in adj:
                for neighbour in adj[node]:
                    if indegree[neighbour]!=0:
                        indegree[neighbour]-=1

                    if indegree[neighbour] ==0:
                        queue.append(neighbour)
        return topological if len(topological) == numCourses else []

        

