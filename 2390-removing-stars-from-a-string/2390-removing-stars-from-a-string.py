class Solution:
    def removeStars(self, s: str) -> str:

        stack = []
        for ch in s:
            if ch =="*":
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)

    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch=="*":
                stack.pop(-1)
            else:
                stack.append(ch)
        return "".join(stack)
        