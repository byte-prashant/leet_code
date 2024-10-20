class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        # can we use insertion sort
        sorted_elems = [float("+inf")]*len(nums)
        pos = -1
        result = []
        def put_element(pos, ele):
            #print("for ele", ele, pos)
            new_elem_pos = pos+1
            pos = pos+1
            sorted_elems[new_elem_pos] = ele
            while(new_elem_pos>0):
                
                if sorted_elems[new_elem_pos]<=sorted_elems[new_elem_pos-1]:
                   
                    sorted_elems[new_elem_pos],sorted_elems[new_elem_pos-1]=sorted_elems[new_elem_pos-1],sorted_elems[new_elem_pos]
                    new_elem_pos-=1
                else:
                    break
            #sorted_elems[new_elem_pos] = ele
            #print(sorted_elems)
            return  pos,new_elem_pos+1

        for ele in nums[::-1]:
            pos,insert_pos = put_element(pos, ele)
            #print("insert pos", pos,insert_pos)
            result.append(insert_pos-1)

        return result[::-1]



    def countSmaller(self, nums: List[int]) -> List[int]:

        # can we use binary sort
        sorted_elems = []
        pos = -1
        result = []
        def binary_search(pos, ele, sorted_elems):
            
            left = 0
            right = len(sorted_elems)-1
            if not sorted_elems:
                sorted_elems = [ele]
                return 0,sorted_elems
            
            while(left<=right):
                mid = left+(right-left)//2
               
                if sorted_elems[mid]< ele:
                    left = mid+1
                else:
                    right = mid-1
           
            sorted_elems = sorted_elems[:left]+[ele]+sorted_elems[left:]



            
            return  left,sorted_elems

        for ele in nums[::-1]:
            insert_pos,sorted_elems = binary_search(pos, ele,sorted_elems)
           
            result.append(insert_pos)

        return result[::-1]



    def countSmaller(self, nums: List[int]) -> List[int]:

        #modified above algo
        sorted_elems = sorted(nums)
       
        result = []
        def binary_search( ele, sorted_elems):
            
            left = 0
            right = len(sorted_elems)-1
            res = -1
            
            while(left<=right):
                mid = left+(right-left)//2
               
                if sorted_elems[mid]< ele:
                    left = mid+1
                elif sorted_elems[mid]>ele :
                    right = mid-1

                else:
                    res = mid
                    right = mid-1
                
           
            


            
            return  res

        for i in range(len(nums)):
            index = binary_search(nums[i],sorted_elems)
            result.append(index)
            sorted_elems.pop(index)

        return result


            
  
    def countSmaller2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)]  # record value and index
        result = [0] * n

        def merge_sort(arr, left, right):
            # merge sort [left, right) from small to large, in place
            if right - left <= 1:
                return
            mid = (left + right) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid, right)
            merge(arr, left, right, mid)

        def merge(arr, left, right, mid):
            # merge [left, mid) and [mid, right)
            i = left  # current index for the left array
            j = mid  # current index for the right array
            # use temp to temporarily store sorted array
            temp = []
            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    # j - mid numbers jump to the left side of arr[i]
                    result[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            # when one of the subarrays is empty
            while i < mid:
                # j - mid numbers jump to the left side of arr[i]
                result[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            while j < right:
                temp.append(arr[j])
                j += 1
            # restore from temp
            for i in range(left, right):
                arr[i] = temp[i - left]

        merge_sort(arr, 0, n)

        return result

        