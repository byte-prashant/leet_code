class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix[::-1])
        matrix[:]   = list(zip(*matrix[::-1]))


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = matrix[::-1]

        matrix[:] = list(zip(*matrix))

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix[0])):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for row in range(len(matrix)):
            for col in range(len(matrix)//2):
                matrix[row][col],matrix[row][len(matrix)-1-col] = matrix[row][len(matrix)-1-col],matrix[row][col]

        