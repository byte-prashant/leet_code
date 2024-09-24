class Solution:
    def calculate(self, s: str) -> int:
        
            def evaluate1(tokens):
                stack = []
                num = 0
                sign = '+'

                while tokens:
                    token = tokens.pop(0)

                    if token.isdigit():
                        num = int(token)

                    if token == '(':
                        # after finishing up with the curly braces eval, we can c onsider it's result as new number as (4+5)==>(9)
                        # 9 is a new num
                        num = evaluate(tokens)

                    if token in '+-*/' or token == ')' or not tokens:
                        if sign == '+':
                            stack.append(num)
                        elif sign == '-':
                            stack.append(-num)
                        elif sign == '*':
                            stack[-1] *= num
                        elif sign == '/':
                            stack[-1] //= num  # Integer division

                        if token == ')':
                            break

                        sign = token
                        num = 0

                return sum(stack)

        # removing stack

            def evaluate(tokens):
                result_stack = 0
                last_element_stack = 0
                num = 0
                sign = '+'

                while tokens:
                    token = tokens.pop(0)

                    if token.isdigit():
                        num = int(token)

                    if token == '(':
                        num = evaluate(tokens)
                        print(num)
                    if token in '+-*/' or token == ')' or not tokens:
                        if sign == '+':
                            result_stack+=last_element_stack
                            last_element_stack = num
                        elif sign == '-':
                            result_stack+=last_element_stack
                            last_element_stack = -num
                        elif sign == '*':
                           last_element_stack *= num
                        elif sign == '/':
                            last_element_stack =int(last_element_stack/ num)  # Integer division

                        if token == ')':
                            break

                        sign = token
                        num = 0
                result_stack+=last_element_stack
                return result_stack

            # Prepare tokens from the input expression
            tokens = []
            i = 0
            expression =s
            while i < len(expression):
                char = expression[i]
                if char.isdigit():
                    num_str = char
                    while i + 1 < len(expression) and expression[i + 1].isdigit():
                        num_str += expression[i + 1]
                        i += 1
                    tokens.append(num_str)
                elif char in '+-*/()':
                    tokens.append(char)
                i += 1
            #print(tokens)
            return evaluate(tokens)

    def calculate(self, s: str) -> int:
        s =s+"+"

        def evaluate(i):
            result_stack = 0
            last_element_stack = 0
            num = 0
            sign = "+"

            while(i<len(s)):
                char = s[i]

                if char.isdigit():
                    num = num*10 + int(char)

                if char == "(":
                    # we can put it following bracket also
                    # but then we need to tak care of val of num
                    # as val of num will not be zero, as we do[at the end, num =0] in exection of following condition
                    # this value of num will available for next execution
                    # we need to consider it as a new integer value, given in exppression
                    num , i = evaluate(i+1)
                    #i=i-1
                    print(num, i, "---------")
                    #continue 

                if char in "+-*/)" or i == len(s)-1:

                    if sign =="+":
                        print("in",i)
                        result_stack +=last_element_stack
                        last_element_stack = num

                    elif sign =="-":
                        result_stack +=last_element_stack
                        last_element_stack = -num

                    elif sign =="*":
                          last_element_stack *= num

                    elif sign == "/":
                        last_element_stack = int(last_element_stack/num)

                    elif sign == ")":
                        break
                        #esult_stack+=last_element_stack
                        #return result_stack ,i

                    sign = char
                    num = 0

                i+=1
                
            result_stack+=last_element_stack
            return result_stack ,i-1

        return evaluate(0)[0]


        
        