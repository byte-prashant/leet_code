from collections import defaultdict
class WordDictionary:

    def __init__(self):
        self.trie =  {}
        self.end = "$"

    def addWord(self, word: str) -> None:
        data = self.trie
        for letter in word:
            data = data.setdefault(letter,{})

        data[self.end] = word

    def explore(self,data,suffix):
        if not suffix :
            if self.end in data:

                return True
            return False

        letter = suffix[0]
        if letter!="." and not letter in data:
            return False

        if letter ==".":
            ans = False
            for key,val in data.items():
                if key!= self.end:
                    ans = ans  or self.explore(data[key],suffix[1:])
            return ans
        
        if letter in data:
            return self.explore(data[letter],suffix[1:])





    def search(self, word: str) -> bool:
        data = self.trie

        return self.explore(data,word)
        
        
            
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)