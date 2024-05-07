class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        print("Inside push", self.minStack)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.minStack[-1]:
                self.minStack.pop()
            self.stack = self.stack[:-1]  # Remove the last element from stack
            print("Inside pop", self.minStack)

    def top(self) -> int:
        if self.stack:
            print("Inside top", self.stack[-1])
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            print("Inside getMin", self.minStack[-1])
            return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin() 
