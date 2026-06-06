class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            ans.extend(word.split(separator))

        ans = [word for word in ans if word]
        return ans

        