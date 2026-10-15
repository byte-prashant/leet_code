import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x : x[1])
        heap = []
        max_time = 0
        for duration, last_day in courses:
            heapq.heappush(heap,-duration)
            max_time += duration
            if max_time > last_day:
                biggest_course = heapq.heappop(heap)
                max_time += biggest_course
        return len(heap)