class Solution:
    def calculate(self, s: str) -> int:

        curr_num = 0
        curr_sign  = "+"
        stack = []
        for i in range(len(s)):
            
            char = s[i]
            if char.isdigit():
                curr_num = (curr_num * 10) + int(char)
                #print(curr_num)


            if  (not char.isdigit() and not s[i].isspace()) or i == len(s)-1:
                print(curr_sign,i, "--")
                if curr_sign == "+":
                    stack.append(curr_num)

                elif curr_sign == "-":
                    stack.append(-curr_num)

                elif curr_sign == "*":
                    stack.append(stack.pop()*curr_num)

                elif curr_sign == "/":
                    #print("you are",abs(stack[-1])//curr_num)
                    stack.append(int(stack.pop()/curr_num))
                curr_num = 0
                curr_sign = char

       # print(stack)
        return sum(stack)
    

    def calculate(self, s: str) -> int:
        print("you are right place")
        prev_sign = "+"
        last_num_stack = 0
        num = 0
        stack = 0 

        for c in s+"+":
            
            if c.isspace():
                continue

            if c.isdigit():
                num = num*10+int(c)
                print(num)

            if c in ["+","-","/","*"]:

                if prev_sign == "+":
                    stack +=last_num_stack
                    last_num_stack = num
                if prev_sign =="-":
                    stack+= last_num_stack
                    last_num_stack = -num

                if prev_sign == "*":
                    last_num_stack = last_num_stack*num

                if prev_sign =="/":
                    last_num_stack = int(last_num_stack/num)

                num =0 
                prev_sign = c

        stack+= last_num_stack
        return stack

    def calculate(self, s: str) -> int:
        curr_res = 0
        res = 0
        num = 0
        op = "+"  # keep the last operator we have seen
        
		# append a "+" sign at the end because we can catch the very last item
        for ch in s + "+":
            if ch.isdigit():
                num = 10 * num + int(ch)

            # if we have a symbol, we would start to calculate the previous part.
            # note that we have to catch the last chracter since there will no sign afterwards to trigger calculation
            if ch in ("+", "-", "*", "/"):
                if op == "+":
                    curr_res += num
                elif op == "-":
                    curr_res -= num
                elif op == "*":
                    curr_res *= num
                elif op == "/":
                    # in python if there is a negative number, we should alway use int() instead of //
                    curr_res = int(curr_res / num)
                
                # if the chracter is "+" or "-", we do not need to worry about
                # the priority so that we can add the curr_res to the eventual res
                if ch in ("+", "-"):
                    res += curr_res
                    curr_res = 0
                
                op = ch
                num = 0
        
        return res


                    
