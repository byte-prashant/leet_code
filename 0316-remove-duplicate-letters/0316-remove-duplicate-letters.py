class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        frequency = Counter(s)
        stack = []

        seen = set()

        for index in range(len(s)):

            ch = s[index]
            frequency[ch]-=1


            if ch in seen:
                continue

            while stack and stack[-1]>ch and frequency[stack[-1]]>=1:
                c = stack.pop()
                seen.remove(c)
               

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)


        