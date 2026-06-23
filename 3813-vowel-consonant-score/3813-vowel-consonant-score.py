class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowel = {"a":1,"e":1,"i":1,"o":1,"u":1}
        v , c=0,0
        for ch in s:
            if ch.isalpha():
                if ch in vowel:
                    v+=1
                else:
                    c+=1
       
        if c>0:
            return floor(v/c)
        return 0 

        