# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:

        # A single integer doesn't need recursive parsing
        if s[0] != "[":
            return NestedInteger(int(s))

        def sol(pos):
            ans = NestedInteger()

            num = 0
            sign = 1
            has_num = False

            while pos < len(s):
                ch = s[pos]

                if ch == ",":
                    if has_num:
                        ans.add(NestedInteger(num * sign))

                    num = 0
                    sign = 1
                    has_num = False

                elif ch == "[":
                    sub_list, pos = sol(pos + 1)
                    ans.add(sub_list)
                    continue

                elif ch == "-":
                    sign = -1

                elif ch.isdigit():
                    num = num * 10 + int(ch)
                    has_num = True

                elif ch == "]":
                    if has_num:
                        ans.add(NestedInteger(num * sign))

                    return ans, pos + 1

                pos += 1

            return ans, pos

        return sol(1)[0]