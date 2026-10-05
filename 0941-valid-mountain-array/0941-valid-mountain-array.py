class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:

    
        
        up = 0
        lst_val = arr[0]


        for val in arr[1:]:

            if up==1 or up ==0 :

                if  lst_val < val:
                    up = 1
                elif lst_val == val:
                    up = 0
                else:
                    if up == 1:
                        up = 2 
                    else:
                        return False
                    

                
            else:

                if  not lst_val > val:
                    return False
            print(up)
            lst_val = val

        return True if up ==2 else False

        


    
                 
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0

        # 1. Climb up
        while i+1 < n and arr[i] < arr[i+1]:
            i += 1

        # 2. Peak check: Peak can't be first or last element
        if i == 0 or i == n-1:
            return False

        # 3. Climb down
        while i+1 < n and arr[i] > arr[i+1]:
            i += 1

        # 4. If we reached the end, it's a mountain
        return i == n-1

        