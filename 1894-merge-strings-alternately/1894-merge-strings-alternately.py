class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1),len(word2))
        new_str = ""
        curr_string,is_word_1 = word1,True
        while(word1 and word2):
            ch = word1[0] if is_word_1 else word2[0]
            new_str = new_str+ch
            if is_word_1:
                word1 = word1[1:]
            else:
                word2 = word2[1:]
            is_word_1 = False if is_word_1 else True 

        new_str = new_str+word2
        new_str = new_str+word1

        return new_str
        