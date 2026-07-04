class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        directions = [(0,1),(1,0)]
        n = len(obstacleGrid[0])
        m= len(obstacleGrid)
        dp = [[0] * n for _ in range(m)]
        def is_valid(x,y):
            return x<m and x>=0 and y>=0 and y<n

        # base case, final index will be 1
        if obstacleGrid[m-1][n-1] == 0 :
            dp[m-1][n-1] = 1 
        else:
            return 0

        # loop, range =>x ==>[0,m],y=>[0,n]
        # order x  dependendant on x+dx, similary y => y+dx

        for x in range(m-1, -1,-1):
            for y in range(n-1,-1,-1):
                # dont recompute base case
                if (x == m - 1 and y == n - 1) or obstacleGrid[x][y]==1:
                    continue

                right = 0
                down = 0

                if y+1 < n:
                    right = dp[x][y+1]

                if x+1 < m:
                    down = dp[x+1][y]

                dp[x][y] = right + down

        return dp[0][0]

    
# dp[x][y] = dp[x][y+1]+dp[x+1][y]
# if current ==> dp[x], next => dp[x+1]
#  current[y] ==> current[y+1]+next[y]       
# as current[y] is not dependend on current[y] we can  create this at every iteration 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [0] * n
        dp[n-1] = 1

        for x in range(m - 1, -1, -1):

            for y in range(n - 1, -1, -1):

                if obstacleGrid[x][y] == 1:
                    dp[y] = 0

                elif x == m - 1 and y == n - 1:
                    continue

                else:

                    right = dp[y + 1] if y + 1 < n else 0
                    down = dp[y]

                    dp[y] = right + down

        return dp[0]