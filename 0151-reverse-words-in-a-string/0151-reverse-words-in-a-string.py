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

    def reverseWords(self, s: str) -> str:
        s=s.strip(" ")
        words = []
        input_str = s.split(" ")[::-1]
        print(input_str)
        for index ,word in enumerate(input_str):
            if word:
                if words:
                    words.append(" ")
                words.append(word)
                
                

        return "".join(words)

    def reverseWords(self, s: str) -> str:
        splitted = s.split()
        reverse = splitted[::-1]
        return " ".join(reverse)

                
               





        