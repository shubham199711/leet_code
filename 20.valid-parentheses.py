#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
par_open = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
}

par_close = {
    ']' : '[',
    '}' : '{',
    ')' : '(',
}

class Solution:
    def isValid(self, s):
        stack = []
        for item in s:
            if item in par_open.keys():
                stack.append(item)
            elif item in par_close.keys():
                if len(stack) > 0 and  par_close.get(item) == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False
        
# @lc code=end

