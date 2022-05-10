class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def isMatchsol(s, p, n, m):

            if n < 0 and m < 0:
                return 1
            if n < 0:
                while (m >= 0):
                    e = p[m]
                    if not e == "*":
                        return 0

                    m -= 1
                return 1
            if n >= 0 and m < 0:
                return 0

            if p[m] == "*":

                return isMatchsol(s, p, n - 1, m) or isMatchsol(s, p, n, m - 1)

            elif p[m] == ".":

                return isMatchsol(s, p, n - 1, m - 1)
            else:
                if s[n] == p[m]:
                    return isMatchsol(s, p, n - 1, m - 1)
                else:
                    return 0

        return isMatchsol(s, p, len(s) - 1, len(p) - 1)