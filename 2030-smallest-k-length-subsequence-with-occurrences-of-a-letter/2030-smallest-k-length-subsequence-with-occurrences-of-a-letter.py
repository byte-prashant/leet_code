class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:

        stack = []

        occ = repetition
        remaining_letter = s.count(letter)
        letter_in_stack = 0
        for  index, ch in enumerate(s):

            if ch == letter:
                remaining_letter -= 1

            remaining = len(s) - index - 1

            while stack and stack[-1]>ch:
                # include cucrrent character at index, also
                # 
                if len(stack)+ remaining <k:
                    break


                
                if stack[-1] == letter:
                    if  letter_in_stack-1+remaining_letter <occ:
                        break

                    letter_in_stack-=1

                stack.pop()
            
            

             # Can we append this character?
            if len(stack) < k:

                if ch == letter:
                    stack.append(ch)
                    letter_in_stack += 1

                elif k - len(stack) > repetition - letter_in_stack:
                    stack.append(ch)

        return "".join(stack[:k])


                    



        