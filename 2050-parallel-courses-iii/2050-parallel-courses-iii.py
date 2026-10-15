class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:


        adj = {}
        indegre = [0 for i in range(n+1)]
        for source,dst in relations:

            if source in adj:
                adj[source].append(dst)
            else:
                adj[source] = [dst]
            
            indegre[dst]+=1

        

        
        queue = []
        required_month = 0
        for course in range(n+1):
            if not indegre[course] and course !=0:
                queue.append(course)

        print(adj)
 
        while queue:
            max_no_of_months = 0
            level = len(queue)
            print(queue,indegre)
            for _ in range(level):
                course  = queue.pop(0)
                if course in adj:
                    for  dependant_course in adj[course]:

                        indegre[dependant_course] -=1

                        if indegre[dependant_course] ==0:

                            queue.append(dependant_course)

                print(course)

                max_no_of_months = max(max_no_of_months,time[course-1])

            required_month+=max_no_of_months

        return required_month
                    

    

class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        adj = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)

        for source, dst in relations:
            adj[source].append(dst)
            indegree[dst] += 1

        # Earliest completion time for each course
        finish = [0] * (n + 1)

        queue = deque()

        for course in range(1, n + 1):
            finish[course] = time[course - 1]

            if indegree[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()

            for dependent in adj[course]:
                finish[dependent] = max(
                    finish[dependent],
                    finish[course] + time[dependent - 1]
                )

                indegree[dependent] -= 1

                if indegree[dependent] == 0:
                    queue.append(dependent)

        return max(finish)

