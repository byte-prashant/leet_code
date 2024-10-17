values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = values.get(s[-1])
        for i in range(len(s) - 2,-1,-1):
            print(i)
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total