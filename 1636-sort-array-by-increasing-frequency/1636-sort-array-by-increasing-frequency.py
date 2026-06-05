class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq_data = [[] for _ in range(len(nums)+1)]
        fre = Counter(nums)

        for ele, f in fre.items():
            freq_data[f].append(ele)

        ans =[]
        for freq , ele in enumerate(freq_data):
            if freq:
                ele.sort(reverse = True)
                for el in ele:
                    count = freq
                    while count>0:
                        ans.append(el)
                        count-=1
        return ans


        