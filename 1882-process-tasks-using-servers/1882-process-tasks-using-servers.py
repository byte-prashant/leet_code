class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        servers = [(weight,index,0) for index , weight in enumerate(servers)]
        busy_servers = []
        import heapq
        heapq.heapify(servers)
        current_time = 0
        ans  = []
        while tasks:
            new_busy_servers = []
            for busy_server  in busy_servers:
                weight, index, time = busy_server
                time-=1
                if time ==0:
                    heapq.heappush(servers,( weight, index, time))
                else:
                    new_busy_servers.append((weight, index, time))
                
            busy_servers = new_busy_servers

            free_server =  heapq.heappop(servers) if servers else None
            print(busy_servers,servers,free_server)
            if free_server:
              
                weight, index, time = free_server
                time  = tasks.pop(0)
                busy_servers.append(( weight, index, time))
                ans.append(index)
        
        return ans


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # maintainig busys server as heap
        # how to update time
        # make a global, clock
        # maintain ext time  while insertion
        # if  global_time<= exit time, free server

        # heap orders on basis of first element
        # list pop shifts elements by n place so slow, use index instead
        servers = [(weight,index,0) for index , weight in enumerate(servers)]
        busy_servers = []
        import heapq
        heapq.heapify(servers)
        heapq.heapify(busy_servers)
        task_queue = []
        current_time = 0
        ans  = []
        while tasks or task_queue:
            while busy_servers and busy_servers[0][0]<=current_time:
                time, weight, index = heapq.heappop(busy_servers)
                
                
                heapq.heappush(servers,( weight, index, 0))
            if tasks:
                task_queue.append(tasks.pop(0))
            while task_queue and servers:
                free_server =  heapq.heappop(servers) if servers else None
                #print(busy_servers,servers,free_server)
                if free_server:
                
                    weight, index, time = free_server
                    time  = task_queue.pop(0)
                    heapq.heappush(busy_servers,( current_time+time,weight, index ))
                    heapq.heapify(busy_servers)
                    ans.append(index)

            current_time+=1
        
        return ans

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # maintainig busys server as heap
        # how to update time
        # make a global, clock
        # maintain ext time  while insertion
        # if  global_time<= exit time, free server

        # heap orders on basis of first element
        # list pop shifts elements by n place so slow, use index instead

        # use deque instead of list
        servers = [(weight,index,0) for index , weight in enumerate(servers)]
        busy_servers = []
        import heapq
        heapq.heapify(servers)
        heapq.heapify(busy_servers)
        task_queue = deque()
        current_time = 0
        ans  = []
        task_index = 0
        while task_index<len(tasks) or task_queue:
            local_time = 1
            while busy_servers and busy_servers[0][0]<=current_time:
                time, weight, index = heapq.heappop(busy_servers)
                
                local_time= max(local_time, time)
                heapq.heappush(servers,( weight, index, 0))
            if task_index <len(tasks):
                task_queue.append(tasks[task_index])
            while task_queue and servers:
                free_server =  heapq.heappop(servers) if servers else None
                #print(busy_servers,servers,free_server)
                if free_server:
                
                    weight, index, time = free_server
                    time  = task_queue.popleft()
                    heapq.heappush(busy_servers,( current_time+time,weight, index ))
                    #heapq.heapify(busy_servers)
                    ans.append(index)
            task_index+=1

            
            current_time += 1
        
        return ans
from collections import deque
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        servers = [(weight, index) for index, weight in enumerate(servers)]
        heapq.heapify(servers)

        busy_servers = []
        task_queue = deque()

        current_time = 0
        task_index = 0
        ans = []

        while task_index < len(tasks) or task_queue or busy_servers:

            while busy_servers and busy_servers[0][0] <= current_time:
                finish_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(servers, (weight, index))

            while task_index < len(tasks) and task_index <= current_time:
                task_queue.append(tasks[task_index])
                task_index += 1

            while task_queue and servers:
                weight, index = heapq.heappop(servers)
                duration = task_queue.popleft()

                heapq.heappush(
                    busy_servers,
                    (current_time + duration, weight, index)
                )

                ans.append(index)

            if not servers and busy_servers:
                current_time = max(current_time + 1, busy_servers[0][0])
            else:
                current_time += 1

        return ans

           

    
        