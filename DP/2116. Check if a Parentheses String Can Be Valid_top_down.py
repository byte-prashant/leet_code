class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        l = len(s)

        # not using this method
        def check_if_valid_parenthesis(strr):

            stk = []

            for i in range(len(strr)):

                if strr[i] == "(":

                    stk.append("(")
                elif strr[i] == "{":
                    stk.append("{")
                elif strr[i] == "[":
                    stk.append("[")

                elif strr[i] == ")":

                    if stk:

                        el = stk.pop()
                        if not el == "(":
                            return False
                    else:
                        return False

                elif strr[i] == "]":

                    if stk:

                        el = stk.pop()
                        if not el == "[":
                            return False
                    else:
                        return False

                elif strr[i] == "}":

                    if stk:

                        el = stk.pop()
                        if not el == "{":
                            return False
                    else:
                        return False
            if not stk:

                return True
            else:
                return False

        def append_new_ele(p, ele):

            if ele == ")":

                if p:
                    p = p[:len(p) - 1]
                    return True, p
                else:
                    return False, p + ")"
            else:
                p = p + "("
                return True, p

        dp = {}

        def solCanBeValid(n, new):

            if n == l:
                # print("new",new,check_if_valid_parenthesis(new))
                return check_if_valid_parenthesis(new)

            if (n, new) in dp:
                return dp[(n, new)]

            if locked[n] == "1":
                bol, new = append_new_ele(new, s[n])
                if bol:
                    y = solCanBeValid(n + 1, new)
                    dp.update({(n, new): y})
                    return y
                else:
                    return False
            else:
                ele = s[n]
                if s[n] == "(":
                    ele = ")"
                else:
                    ele = "("
                bol, new1 = append_new_ele(new, ele)
                b2 = b1 = False
                if bol:
                    b1 = solCanBeValid(n + 1, new1)
                boll, new2 = append_new_ele(new, s[n])

                if boll:
                    b2 = solCanBeValid(n + 1, new2)

                # print("b1",b1,"b2",b2,"nw2",new2)
                dp.update({(n, new): b1 or b2})

                return b1 or b2

        return solCanBeValid(0, "")









