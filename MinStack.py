class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        _min = min(self.minStack[-1] if self.minStack else 0, val)
        self.minStack.append(_min)
        
    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]