class Solution:
    def decodeString(self, s: str) -> str:

        def decode(index):
            stack = []
            curr_str = ""
            num = 0
            for c in s:
                if c.isdigit():
                    num =num *10 + int(c)

                elif c =="[":
                    stack.append(num)
                    stack.append(curr_str)
                    num = 0
                    curr_str = ""
                elif c == "]":
                    prev_str = stack.pop()
                    freq = stack.pop()
                    
                    curr_str = prev_str + curr_str * freq

                else:
                    curr_str += c


                print(curr_str)


            # while stack:
            #     curr_str = stack.pop() + curr_str

            

            return curr_str


        return decode(0)