class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        def is_valid(row, col):
            return row>=0 and row<len(grid) and col>=0 and col<len(grid[0])
        
        visited = {}
        ans = []
        def dfs(row, col, initial_col):

            if  not is_valid(row, col):
                return 0

            if (row,col) in visited:
                return

            if grid[row][col] == initial_col:
                visited[(row,col)] = 1
                count = 0
                if is_valid(row+1, col) and grid[row+1][col] == initial_col:
                    dfs(row+1,col,initial_col)
                else:
                    count+=1

                if is_valid(row-1, col) and grid[row-1][col] == initial_col:
                    dfs(row-1,col,initial_col)
                else:
                    count+=1

                if is_valid(row, col+1) and grid[row][col+1] == initial_col:
                    dfs(row,col+1,initial_col)
                else:
                    count+=1

                if is_valid(row, col-1) and grid[row][col-1] == initial_col:
                    dfs(row,col-1,initial_col)
                else:
                    count+=1

                if count>0:
                   ans.append((row,col))

            return

        orig = grid[row][col]
        dfs(row, col , grid[row][col])
        #grid[row][col] = orig
        for row, col in ans:
            grid[row][col] = color
        return grid





                



