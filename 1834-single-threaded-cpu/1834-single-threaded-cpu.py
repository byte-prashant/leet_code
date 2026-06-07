class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        tasks = sorted(
            [(enq, proc, i) for i, (enq, proc) in enumerate(tasks)]
        )
        task_queue = []
        current_task = 0
        current_time = 0
        ans = []
        dp = {}
        index= 0
        while index<len(tasks) or task_queue or current_task>0:

            current_time+=1
            while index<len(tasks)  and tasks[index][0] <= current_time:
                enq_time, proce_time ,index_task= tasks[index]
                   
                heapq.heappush(task_queue,(proce_time ,index_task))

                index+=1
                   
                   
            if current_task:
                current_task-=1
            #print(task_queue,current_time, current_task)
            if current_task<=0 and task_queue:
                # pick up the task
                heapq.heapify(task_queue)
                proce_time ,index_task = heapq.heappop(task_queue)
              
                current_task = proce_time
                ans.append(index_task)
            
            
           
        
        return ans


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        tasks = sorted(
            [(enq, proc, i) for i, (enq, proc) in enumerate(tasks)]
        )
        task_queue = []
        current_task = 0
        current_time = 0
        ans = []
        dp = {}
        index= 0
        while index<len(tasks) or task_queue or current_task>0:

            if not task_queue and current_time < tasks[index][0]:
                current_time = tasks[index][0]
                #index+=1

            while index<len(tasks)  and tasks[index][0] <= current_time:
                enq_time, proce_time ,index_task= tasks[index]
                   
                heapq.heappush(task_queue,(proce_time ,index_task))

                index+=1
            

            proce_time ,index_task = heapq.heappop(task_queue)
            current_time += proce_time
            ans.append(index_task)
            
            
           
        
        return ans





        





        