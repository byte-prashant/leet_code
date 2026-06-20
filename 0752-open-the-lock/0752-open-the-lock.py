class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        right_move = {0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:0}
        left_move = {0:9,1:0,2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8}
        visited = { key:1 for key in deadends}
        if "0000" in visited:
            return -1
        if "0000" == target:
            return 0
        queue = deque()
        queue.append(([0,0,0,0],0))

        while queue:
            #print(queue.popleft())
            wheels ,turns =  queue.popleft()

            key = "".join(map(str,wheels))
            visited[key] =1
            for wheel,_key in enumerate(wheels):
                
                left_state = wheels[:]
                left_state[wheel] = left_move[_key]
                key  = "".join(map(str,left_state))
                if key == target:
                    return turns+1
                if not key in visited:
                    queue.append((left_state,turns+1))
                    visited[key] =1
                right_state = wheels[:]
                right_state[wheel] = right_move[_key]
                key  = "".join(map(str,right_state))
                if key == target:
                    return turns+1
                if not key in visited:
                    queue.append((right_state,turns+1))
                    visited[key] =1

        return -1







            
        