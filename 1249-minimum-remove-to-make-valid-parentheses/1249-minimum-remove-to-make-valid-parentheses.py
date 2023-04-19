class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        c = list(s)
        stack, open_index = [], []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
                open_index.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                    open_index.pop()
                else:
                    c[i] = ''
        for i in open_index:
            c[i] = ''
        return "".join(c)