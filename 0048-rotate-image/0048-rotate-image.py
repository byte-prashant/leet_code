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
        