class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        string_length = len(s)
        for i in range(1, string_length//2 +1):

            if string_length %i ==0:
                new_str  = s[:i] *(string_length//(i))
                print(s[:i+1], (string_length//i))
                if new_str ==s:
                    return True


        return False


        