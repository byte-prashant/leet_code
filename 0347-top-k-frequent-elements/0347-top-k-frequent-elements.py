class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter
        frequencies = Counter(nums)
        frequencies = [(elem, freq) for elem ,freq in frequencies.items()]

        # using quick select
        # this is not quick select
        # but as order does not matter we do not need to sort it fully
        # we can use quick select
        # and pick always right side, untill lenght is k
        frequencies.sort(key = lambda x: x[1])
        #print(frequencies)
        return [ ele[0] for  ele in frequencies[len(frequencies)-k:]]

    # trying quick select
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter
        frequencies = Counter(nums)
        frequencies = [(elem, freq) for elem ,freq in frequencies.items()]

        # using quick select
        # but as order does not matter we do not need to sort it fully
        # we can use quick select
        # and pick always right side, untill lenght is k
        last_elem = None
        while len(frequencies)>k:
            pivot ,last_elem= frequencies[-1][1],frequencies[-1]
            frequencies = [ ele for ele in frequencies if ele[1]>pivot ]
            


        return [ ele[0] for  ele in frequencies] if frequencies else [last_elem[0]]
        