class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        for index  in range(len(s2)-len(s1)+1):
            freq_s1 = Counter(s2[index :index+len(s1)])
            freq_s2 = Counter(s1)
            print(freq_s1)
            if freq_s1 == freq_s2:
                return True
        
        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window = {}
        target =  Counter(s1)
        left = 0
        for right  in range(len(s2)):
            window[s2[right]] =  window.get(s2[right],0)+1
            if right - left +1 >len(s1):
                if s2[left] in window:
                    window[s2[left]]-=1
                    if  window[s2[left]] == 0:
                        del  window[s2[left]]
                left+=1
            
            if window == target:
                return True

            
        
        return False
        