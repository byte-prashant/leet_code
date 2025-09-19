class Solution:
    def reverseVowels(self, s: str) -> str:
        def is_vowel(ch):
            ch = ch.lower()
            if ch in ["a","e","i","o","u"]:
                return True
            return False

        left = 0
        right = len(s)-1
        l_s = [ch for ch in s]
        while(left<right):
            if is_vowel(s[left]) and is_vowel(s[right]):
                l = s[left]
                r = s[right]
                l_s[left] = r
                l_s[right] = l

                left+=1
                right-=1

            if left < len(s) and not is_vowel(s[left]):
                left+=1

            if right <len(s) and not is_vowel(s[right]) :
                right-=1

        return "".join(l_s)
        