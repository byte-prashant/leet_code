class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        def sol():
            schedules = []
            for time in intervals:
                schedules.append((time[0],1))
                schedules.append((time[1],-1))

            schedules.sort()
            
            rooms = 0
            max_room = 0
            for time in  schedules:
                    rooms += time[1]
                    max_room = max(max_room,rooms)
                

            return max_room

        def sol1():
            
            s = []
            for int in intervals:
                s.append((int[0], "start")); s.append((int[1], "end"))

            s.sort()
            count,result = 0,0
            for time,type in s:
                if type == "start":
                    count +=1
                    result = max(result, count)
                elif type == "end":
                    count -=1

            return result

        return sol()
