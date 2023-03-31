class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item in ['(', '[', '{']:
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                if item == ')' and stack[-1] == '(':
                    stack.pop(-1)
                elif item == ']' and stack[-1] == '[':
                    stack.pop(-1)
                elif item == '}' and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
        return not(len(stack) > 0)