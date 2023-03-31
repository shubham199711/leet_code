class MyQueue:
    def __init__(self):
        self.mainStack = []
        self.copy = []
        
    def push(self, x):
        self.copy.append(x)

    def pop(self):
        if len(self.mainStack) > 0:
            return self.mainStack.pop(-1)
        else:
            self.peek()
            if len(self.mainStack) > 0:
                return self.mainStack.pop(-1)
        return -1
        
    def peek(self):
        if len(self.mainStack) > 0:
                return self.mainStack[-1]
        for _ in range(len(self.copy)):
            self.mainStack.append(self.copy.pop(-1))
        if len(self.mainStack) > 0:
                return self.mainStack[-1]
        
    def empty(self):
        return len(self.mainStack) == 0 and len(self.copy) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()