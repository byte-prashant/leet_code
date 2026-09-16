class Solution:
    def calculate(self, s: str) -> int:
        
        val =0
        total = 0
        for ch in s:
            if not ch:
                continue
            if ch.isdigit():
                val  = int(ch)
                # if val:
                #     val  = val+ int(ch)*10
                # else:
                #     val  = int(ch)


            elif  ch in {"(":1,")":1}:
                continue
            elif ch in {"+":1,"-":1}:
                if ch =="-":
                    total = total - val
                if ch == "+":
                    total = total + val
                val  = 0
        return total


class Solution:
    def calculate(self, s: str) -> int:
        
        val =0
        total = 0
        curr_ch ="+"
        for ch in s+"+":
            if ch.isdigit():
                val = val*10+int(ch)

            elif ch  in {"(":1,")":1}:
                continue

            elif ch in ["+","-"]:
                if curr_ch == "-":
                    total-=val
                else:
                    total+=val
                
                curr_ch = ch
                val = 0

        return total

class Solution:
    def calculate(self, s: str) -> int:

        def evaluate(pos):
            stack = []
            num = 0
            sign = '+'

            while pos < len(s):
                token = s[pos]

                if token.isdigit():
                    num = num * 10 + int(token)

                if token == '(':
                    num, pos = evaluate(pos + 1)

                if token in '+-*/)' or pos == len(s) - 1:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] *= num
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / num)

                    num = 0
                    sign = token

                if token == ')':
                    return sum(stack), pos

                pos += 1

            return sum(stack), pos

        return evaluate(0)[0]