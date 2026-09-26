class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:




        def sol(expression):

            if not expression:
                return []

            if not "+" in expression and not  "-" in expression and not "*" in expression and not "/" in expression:
                return [int(expression)]

            if len(expression) == 1:
                return [int(expression)]

            temp = []
            for pos in range(len(expression)):

                if not expression[pos].isdigit():
                    op = expression[pos]
                    left = sol(expression[:pos])
                    right = sol(expression[pos+1:])

                    for l in left:
                        for r in right:
                            if op=="+":
                                temp.append(l+r)
                            if op=="*":
                                temp.append(l*r)
                            if op =="-":
                                temp.append(l-r)
            return temp

        return sol(expression)
                            



        