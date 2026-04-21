class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        visited = {key:False for key in range(len(graph))}
       
        safe_nodes = []
        def dfs(node):
            #print("---node",node)
            if visited[node]:
                if node in safe_nodes:
                    return True
                return False
            
           
            
            is_safe = True
            visited[node] = True
            for next_node in graph[node]:
                if not dfs(next_node):
                    return False

            if not node in safe_nodes and is_safe:
                    safe_nodes.append(node)
            #print("is_safe---",node,is_safe)
            return is_safe

        for node in range(len(graph)):
            dfs(node)
        safe_nodes.sort()
        return safe_nodes

    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        visited = [0 for key in range(len(graph))]
       
     
        def dfs(node):
            #print("---node",node)
            if visited[node]:
                return visited[node] == 2
            
           
            is_safe = True
            visited[node] = 1
            for next_node in graph[node]:
                if not dfs(next_node):
                    return False

            visited[node] = 2
            #print("is_safe---",node,is_safe)
            return is_safe

        
        return [ i for i in range(len(graph)) if dfs(i)]

        