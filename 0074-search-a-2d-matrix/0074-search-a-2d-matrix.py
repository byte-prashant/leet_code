class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        def binary_search(row, target):
            left = 0
            right = len(row)-1

            while(left<=right):
               
                mid = left+ (right-left)//2
                
                if row[mid] == target:
                    return mid

                elif row[mid] > target:
                    right = mid-1

                else:
                    left = mid+1


            return -1


        for row in matrix:
           
            if target <=row[-1]:
                mid = binary_search(row, target)
    
                if mid == -1:
                    return False
                return True

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left ,right = 0,  len(matrix)*len(matrix[0]) -1
        n = len(matrix[0])
        
        while left<=right:
            mid = (left+right)//2

            mid_row,mid_col = mid//n, mid%n


            if matrix[mid_row][mid_col] == target:
                return True
            elif target<matrix[mid_row][mid_col]:
                right = mid-1

            else:
                left = mid+1


        return False
