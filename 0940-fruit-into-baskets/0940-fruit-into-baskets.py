class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        # time limit exceeded
        max_fruits = 0

        for start in range(len(fruits)):
            buckets= {}
            for pos in range(start, len(fruits)):
                tree= fruits[pos]
                if not tree in buckets:
                    if len(buckets)<2:
                        buckets[tree] =1
                    else:
                        break

                else:
                    buckets[tree]+=1

            max_fruits = max(max_fruits, sum(list(buckets.values())))


        return max_fruits


    def totalFruit(self, fruits: List[int]) -> int:

        # time limit exceeded
        max_fruits = 0
        left = 0
        bucket= {}
        for right in range(len(fruits)):
            
            bucket[fruits[right]] = bucket.get(fruits[right],0)+1 
            
            if len(bucket)>2:
                new_bucket = {}
                new_bucket[fruits[right]] = 1
                left= right-1
                while(fruits[left-1] == fruits[right-1]):
                    left-=1
                new_bucket[fruits[right-1]] = right-left
                
                left+=1
                bucket = new_bucket
            max_fruits = max(max_fruits, sum(list(bucket.values())))


        return max_fruits



    def totalFruit(self, fruits: List[int]) -> int:

        # time limit exceeded
        max_fruits = 0
        left = 0
        bucket= {}
        for right in range(len(fruits)):
            
            bucket[fruits[right]] = bucket.get(fruits[right],0)+1 
            
            if len(bucket)>2:
            
                bucket[fruits[left]]-= 1

                if bucket[fruits[left]] == 0:
                    del bucket[fruits[left]]
                
                left+=1
             
           


        return right-left+1

        