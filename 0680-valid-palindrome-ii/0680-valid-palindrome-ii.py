class Solution:
    def validPalindrome(self, s: str) -> bool:


        def is_valid(s,is_deleted):
            #print(s)
            if len(s)==1:
                return True
            if len(s)==2 :
                if s[0]==s[1]:
                    return True
                else:
                    if not is_deleted:
                        return True
                    return False
                
            end = len(s)-1
            #print(s,end)
            if s[0]==s[end]:
                return is_valid(s[1:end],is_deleted)
            else:
                if not is_deleted:
                    return  is_valid(s[1:],True)  or   is_valid(s[:end],True)
                else:
                    return False

        return is_valid(s,False)


        def validPalindrome(self, s: str) -> bool:

            left =0
            right = len(s)-1

            while left<right:

                if s[left]!=s[right]:
                    left_skip = s[left+1:]
                    right_skip= s[:right]

                    return left_skip == left_skip[::-1] or right_skip == right_skip[::-1]

            return True





        