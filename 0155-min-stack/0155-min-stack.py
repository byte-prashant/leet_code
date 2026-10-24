class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []
        

    def push(self, value: int) -> None:

        if not self.min_stack  or self.min_stack[-1]> value:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

        self.stack.append(value)





        

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            self.min_stack.pop()
            return val
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:

        if self.min_stack:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()