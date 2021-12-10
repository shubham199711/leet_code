from typing import *
#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_element = min(self.stack)
        return None

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.min_element = min(self.stack) if len(self.stack) > 0 else -1

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        return self.min_element


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

