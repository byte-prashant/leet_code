class Solution:
    def reverseWords(self, s: str) -> str:
        words= []
        word = ""
        for ch in s:
            if not  ch == " ":
                
                 word +=ch
                
                   
            else:
                if word:
                   
                    words.append(word)
                    word = ""
        if word:
            words.append(word)
       
        return " ".join(words[::-1])
               





        