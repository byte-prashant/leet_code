class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        dp = [[0 for i in range(len(matrix[0])+1)] for k in range(len(matrix)+1)]
        
        # other wise we could have also made dp matrix one size bigger than the orioginal one
        # then we shoild iterate the matrix from the first position
        # for both  column and rows

        # we can optimmize space here
        #  we are only using the ast row

        max_sqr=0
       
        for r in range(1,len(matrix)+1):
            for c in range(1,len(matrix[0])+1):
                
                if matrix[r-1][c-1] =="1":
                    dp[r][c] = min(dp[r-1][c],dp[r][c-1],dp[r-1][c-1])+1
                    max_sqr = max(max_sqr, dp[r][c])

        return max_sqr*max_sqr



# one soution coulb be exploring all possible sqr matrices, then checking if all nos are 1 or 0
# the find biggest size of the matrix having all ones
#nm toexlore all coordinates start point of rectagle
# then further n*m to explore all possible height and width
# then  n*m to exloreall elements of submatrixs
#total complexity n3m3


# second aproach
# --1) in  first solution we will be exploring all matrices of same size( it do not matter if it contains all 0 or all ones)
# so first learning is , if we have found a matrix with 1*1 size then explore for 2*2  from same postion and so on[ and stop searching for more 1*1]
#https://leetcode.com/problems/maximal-square/solutions/539617/Sliding-window.-99.89.-Very-intuitive-solution-with-explanation


#

