class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        def binary_search(row, target):
            left = 0
            right = len(row)-1

            while(left<=right):
                print(left)
                mid = left+ (right-left)//2
                
                if row[mid] == target:
                    return mid

                elif row[mid] > target:
                    right = mid-1

                else:
                    left = mid+1

                print(left, right)

            

            return -1


        for row in matrix:
            print(target <=row[-1])
            if target <=row[-1]:
                mid = binary_search(row, target)
                print(mid, "--------")
                if mid == -1:
                    return False
                return True

        return False
