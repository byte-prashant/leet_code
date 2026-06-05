class Solution:
    def repeatedCharacter(self, s: str) -> str:
        sett = set()
        for ch in s:
            if not ch in sett:
                sett.add(ch)

            else:
                return ch
        