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

# cover to bootom up
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        directions = [(0,1),(1,0)]

        dp = [[0] * n for _ in range(m)]
        def is_valid(x,y):
            return x<m and x>=0 and y>=0 and y<n

        # base case, final index will be 1

        dp[m-1][n-1] =1

        # loop, range =>x ==>[0,m],y=>[0,n]
        # order x  dependendant on x+dx, similary y => y+dx

        for x in range(m-1, -1,-1):
            for y in range(n-1,-1,-1):
                if x == m - 1 and y == n - 1:
                    continue

                right = 0
                down = 0

                if y+1 < n:
                    right = dp[x][y+1]

                if x+1 < m:
                    down = dp[x+1][y]

                dp[x][y] = right + down

        return dp[0][0]



        

       
      

            

        