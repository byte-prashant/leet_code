class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
            len_hash_map = {}
            def recur(subset, pos):
               
                if pos>=len(nums):
                   
                    len_hash_map[len(subset)] = len_hash_map.get(len(subset),0)+1

                    return
                if not subset or (subset and nums[pos] >subset[-1]) :
                    recur(subset + [nums[pos]], pos+1)
                recur(subset, pos+1)
                
                


                return

            recur([], 0)
           
            max_len = 0
            for key , val in len_hash_map.items():
                max_len = max(max_len,key)

            return len_hash_map[max_len]



    def findNumberOfLIS(self, nums: List[int]) -> int:
        
            len_hash_map = {}
            def recur(prev, pos,count):
               
                if pos>=len(nums):
                    
                    len_hash_map[count] = len_hash_map.get(count,0)+1

                    return


                if  nums[pos] > prev :
                    recur(nums[pos], pos+1, count+1)
                recur(prev, pos+1, count)
                
                

                return

            recur(float("-inf"), 0, 0)
           
            max_len = 0
            for key , val in len_hash_map.items():
                max_len = max(max_len,key)

            return len_hash_map[max_len]




    def findNumberOfLIS(self, nums: List[int]) -> int:
        
            hash_map = {}

            def recur(prev, pos):
                if (prev, pos) in hash_map:
                    return hash_map[(prev, pos)]

               
                if pos>=len(nums):
                    
                    

                    return 0, 1            # subseq of zero lenght, have count 1

                taken_length, taken_count = 0, 0
                if  nums[pos] > prev :
                    taken_length, taken_count = recur(nums[pos], pos+1)
                    taken_length+=1

                not_taken_length, not_taken_count = recur(prev, pos+1)

                
                if taken_length > not_taken_length:
                     hash_map[(prev, pos)] = (taken_length, taken_count)

                elif taken_length == not_taken_length:
                      hash_map[(prev, pos)] = (taken_length, taken_count+not_taken_count)

                else:
                     hash_map[(prev, pos)] = (not_taken_length, not_taken_count)

                return hash_map[(prev, pos)]




                
                

                return

            return recur(float("-inf"), 0)[1]
           
           





