class Solution:
    def convert(self, s: str, numRows: int) -> str:

        hash_map = {}
        rows = numRows
        couter = 1
        row = 1
        for  index in range(len(s)):
            
            char = s[index]
            hash_map[row] = hash_map.get(row,"")+char
            if row == numRows:
                counter = -1
            if row == 1:
                counter = 1
            row+=counter
        new_str = ""
        for key, val in hash_map.items():
            new_str+=val

        return new_str



        