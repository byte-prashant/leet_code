class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        rows = [{} for _ in range(len(board))]
        cols = [{} for _ in range(len(board))]
        boxes = [{} for _ in range(len(board))]


        def get_box(row,col):

            box_r ,box_c= row//3, col//3

            return  box_r*3+box_c

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                box = get_box(row, col)
                if val.isdigit():
                    if val not in rows[row] and val not in cols[col] and val not in boxes[box]:
                        rows[row][val] =1
                        cols[col][val] =1
                        boxes[box][val] =1
                    else:
                        return False
        return True
        