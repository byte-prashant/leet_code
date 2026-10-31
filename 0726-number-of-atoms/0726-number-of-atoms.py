class Solution:
    def countOfAtoms(self, formula: str) -> str:


        def sol(pos):

            element_freq= {}

            current_elem = ""
            current_elem_count = 0

            while pos <len(formula):
                ch = formula[pos]

                if ch.isalpha() :
                    if ch.isupper():
                        if current_elem:
                            current_elem_count= max(current_elem_count,1)
                            element_freq.update({current_elem:current_elem_count})
                            current_elem_count=0
                            current_elem = ch
                        else:
                            current_elem+=ch
                    else:
                        current_elem+=ch
                elif ch.isdigit():
                    digit = int(ch)
                    current_elem_count=current_elem_count*10+digit

                elif ch == "(":
                    sub_elem_freq,pos = sol(pos+1)
                    new_elem = {}
                    mul = 0
                    while pos<len(formula) and formula[pos].isdigit():
                            mul = mul*10+ int(formula[pos])
                            pos+=1
                    if mul>0:
                        for key, val in sub_elem_freq.items():
                            new_elem.update({key:val*mul})

                    
                    for key,val in new_elem.items():
                        if key in element_freq:
                            val = val+element_freq[key]
                        element_freq.update({key:val})
                    print("-------------",new_elem,sub_elem_freq,element_freq,pos,mul)
                        
                    continue
                elif ch == ")":

                    if current_elem:
                        current_elem_count= max(current_elem_count,1)
                        if current_elem in element_freq:
                            current_elem_count +=element_freq[current_elem]
                        element_freq.update({current_elem:current_elem_count})

                    return element_freq,pos+1

                pos+=1

            
            if current_elem:
                current_elem_count= max(current_elem_count,1)
                if current_elem in element_freq:
                    current_elem_count +=element_freq[current_elem]
                element_freq.update({current_elem:current_elem_count})
            return element_freq,pos




        freq,pos = sol(0)
        keys = sorted(key for key,val in freq.items())
        ans = ""

        for key in keys:
            
            if freq[key]>1:
                key =key+str(freq[key])
            ans+=key

        return ans

class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def sol(pos):

            element_freq = {}

            current_elem = ""
            current_elem_count = 0

            while pos < len(formula):
                ch = formula[pos]

                if ch.isalpha():
                    if ch.isupper():
                        if current_elem:
                            current_elem_count = max(current_elem_count, 1)
                            element_freq[current_elem] = (
                                element_freq.get(current_elem, 0) + current_elem_count
                            )

                        current_elem_count = 0
                        current_elem = ch

                    else:
                        current_elem += ch

                elif ch.isdigit():
                    digit = int(ch)
                    current_elem_count = current_elem_count * 10 + digit

                elif ch == "(":
                    # Save previous element before processing group
                    if current_elem:
                        current_elem_count = max(current_elem_count, 1)
                        element_freq[current_elem] = (
                            element_freq.get(current_elem, 0) + current_elem_count
                        )
                        current_elem = ""
                        current_elem_count = 0

                    sub_elem_freq, pos = sol(pos + 1)

                    mul = 0
                    while pos < len(formula) and formula[pos].isdigit():
                        mul = mul * 10 + int(formula[pos])
                        pos += 1

                    mul = max(mul, 1)

                    for key, val in sub_elem_freq.items():
                        element_freq[key] = element_freq.get(key, 0) + val * mul

                    # pos already points to next unprocessed character
                    continue

                elif ch == ")":

                    if current_elem:
                        current_elem_count = max(current_elem_count, 1)
                        element_freq[current_elem] = (
                            element_freq.get(current_elem, 0) + current_elem_count
                        )

                    return element_freq, pos + 1

                pos += 1

            if current_elem:
                current_elem_count = max(current_elem_count, 1)
                element_freq[current_elem] = (
                    element_freq.get(current_elem, 0) + current_elem_count
                )

            return element_freq, pos

        freq, pos = sol(0)

        keys = sorted(freq.keys())
        ans = ""

        for key in keys:
            ans += key
            if freq[key] > 1:
                ans += str(freq[key])

        return ans