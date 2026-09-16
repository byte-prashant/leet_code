class Solution:

    import math

    def evalRPN(self, tokens: list[str]) -> int:

        def is_integer(value):
            try:
                int(value)
                return True
            except ValueError:
                return False

        stack = []

        for tok in tokens:

            if is_integer(tok):
                stack.append(int(tok))

            elif tok == "+":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 + v1)

            elif tok == "-":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 - v1)

            elif tok == "/":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2 / v1))

            elif tok == "*":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 * v1)

        return stack[-1]