class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] ==0:
                    pos.append((row,col))

        rows = [0]*len(matrix)
        cols = [0]*len(matrix[0])

        for row, col in pos:
            if not rows[row]:
                matrix[row] = [0]*len(matrix[0])
                rows[row] = 1
            if not cols[col]:
                cols[col] = 1

                for r in range(len(matrix)):
                    matrix[r][col]  =0 

        return matrix

                

