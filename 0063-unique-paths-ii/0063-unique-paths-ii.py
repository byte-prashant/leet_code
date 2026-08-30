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

        next = [0] * n
        next[n-1] = 1

        for x in range(m - 1, -1, -1):

            current = [0] * n

            for y in range(n - 1, -1, -1):

                if obstacleGrid[x][y] == 1:
                    current[y] = 0

                elif x == m - 1 and y == n - 1:
                    continue

                else:

                    right = current[y + 1] if y + 1 < n else 0
                    down = next[y]

                    current[y] = right + down

            next = current

        return next[0]

# from two rows to one
# current[y] =current[y+1]+next[y]
# current is dependent on same row, so, one row could be possibel
#  and  the  left index is dependent on right
# dp[y] = dp[y]+dp[y+1]
# next[y] will not be over ridden
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

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ans = [0]
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        directions = [(0,1),(1,0)]

        def is_valid(x, y):

            return x<rows and x>=0 and y>=0 and y<cols and not obstacleGrid[x][y]
        dp = {}
        def sol(row, col):

            if row == rows-1 and col == cols-1 and not obstacleGrid[row][col]:
                return 1

            if  (row,col) in dp :
                return dp[(row,col)]

            count = 0
            for dx, dy in directions:

                new_r,new_c = row+dx,col+dy

                if is_valid(new_r, new_c):
                    count+=sol(new_r,new_c)
                       
            dp[(row,col)] = count

            return   dp[(row,col)]
        if obstacleGrid[0][0]==1:
            return 0
        return sol(0,0)




            