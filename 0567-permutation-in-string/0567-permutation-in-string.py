class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        for index  in range(len(s2)-len(s1)+1):
            freq_s1 = Counter(s2[index :index+len(s1)])
            freq_s2 = Counter(s1)
            print(freq_s1)
            if freq_s1 == freq_s2:
                return True
        
        return False
        