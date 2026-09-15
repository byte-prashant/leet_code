class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frq = Counter(arr)

        values = dict(sorted(frq.items(),  key= lambda x: x[1]))
        count = 0
        remove = k
        for key, freq in values.items():
            if remove>=freq:
                remove-=freq
            else:
                if freq-remove>0:
                    remove =0
                    count+=1

        return count
            