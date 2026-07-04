class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        directions = [(0,1),(1,0)]

        def is_valid(x,y):
            return x<m and x>=0 and y>=0 and y<n

        dp = {}
        def sol(x,y):

            if x==m-1 and y==n-1:
                return 1

            if (x,y) in dp:
                return dp[(x,y)]

            count =0
            for dx, dy in directions:

                if is_valid(x+dx,y+dy):
                    count+= sol(x+dx,y+dy)

            dp[(x,y)] = count

            return dp[(x,y)]

        return sol(0,0)

            

        