class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        string = "balloon"
        count = 0
        text_frequency = Counter(text)
        string_freq = Counter(string)
        possile_count = float("+inf")
        string_freq = [[key,val] for key, val in string_freq.items()]
       # print(string_freq,text_frequency)
        for key, val in string_freq:
            if key in text_frequency:
                if text_frequency[key]>=val:
                    possile_count=min(possile_count,text_frequency[key]//val)
                else:
                    return 0
            else:
                return 0
        
        return possile_count

        