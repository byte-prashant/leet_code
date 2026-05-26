class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_brack = []
        remove_indexes = []
        count =0
        new_str = s
        pos = 0
        for index, ch in enumerate(s):
            if ch == ")":
                if open_brack:
                   open_brack.pop(-1)
                else:
                   remove_indexes.append(index)
            elif ch == "(":
                open_brack.append(index)
        if open_brack:
            remove_indexes.extend(open_brack)
        new_s = s
        
        if remove_indexes:
            new_s =""
            
            for index , ch in  enumerate(s):
                if not index in remove_indexes:
                    new_s+=ch

        return new_s
                

        

        

        

        
                

        