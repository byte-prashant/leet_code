class Solution:
    import bisect

    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        
        asteroids = sorted(asteroids)
        print(asteroids)
        start , end = 0 , len(asteroids)
        collide =True
        while(collide and asteroids):
            
            mid = bisect.bisect_right(asteroids, mass, start, end)
          
            print(start, end , mid, mass)
            if (mid< len(asteroids) and mid>start):
                if asteroids[mid-1]<=mass:
                    
                    mass+=sum(asteroids[start:mid])
                    start = mid 
            else:
                if mid==start  :
                    return False
                else:
                    return True

        else:
            if mid>len(asteroids)-1:
                return True

       
        return False

    def asteroidsDestroyed1(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if mass >= asteroid:
                mass += asteroid
            else:
                return False
        return True


    def asteroidsDestroyed1(self, mass: int, asteroids: List[int]) -> bool:
        import heapq
        heapq.heapify(asteroids)
        for i in range(len(asteroids)):
            next_asteroid = heapq.heappop(asteroids)
            if next_asteroid > mass:
                return False
            mass += next_asteroid
        return True