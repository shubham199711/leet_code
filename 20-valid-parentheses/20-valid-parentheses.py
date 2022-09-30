class Solution:
    def isValid(self, s: str) -> bool:
        openPar = set(['(', '{', '['])
        closePar = set([')', '}', ']'])
        stack = []
        indexOpen = {
            '(': 1,
            '{': 2,
            '[': 3,
        }
        indexClose = {
            ')': 1,
            '}': 2,
            ']': 3,
        }
        for char in s:
            if char in openPar:
                stack.append(char)
            elif char in closePar:
                if len(stack) > 0 and indexOpen.get(stack[-1]) == indexClose.get(char):
                    stack.pop()
                else:
                    return False
        return False if len(stack) > 0 else True
                
        