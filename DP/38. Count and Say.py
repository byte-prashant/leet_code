class Solution:
    def countAndSay(self, n: int) -> str:

        def say(n):

            if n == 1:
                return "1"
            if n == 2:
                return "11"

            s = say(n - 1)
            print(s)

            prev = s[0]
            count = 1
            say_s = ""
            for i in range(1, len(s)):
                print(i)
                if prev == s[i]:
                    count = count + 1

                else:
                    say_s = say_s + str(count) + str(prev)
                    prev = s[i]
                    count = 1

            say_s = say_s + str(count) + str(prev)
            return say_s

        return say(n)





