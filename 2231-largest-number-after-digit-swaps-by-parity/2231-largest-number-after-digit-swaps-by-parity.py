class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(digit) for digit in str(num) ]
        even = sorted([d for d in digits if d%2==0], reverse = True)
        odd = sorted([d for d in digits if d%2!=0], reverse = True)
        ans = []
        for digit in digits:
            if digit %2==0:
                ans.append(str(even.pop(0)))
            else:
                ans.append(str(odd.pop(0)))

        return int("".join(ans))


        