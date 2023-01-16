class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ''
        allowed = ['-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for index,item in enumerate(s.strip()):
            if index > 0 and (item == '+' or item == '-'): break
            if item in allowed:
                ans += item
            else:
                break
        if not ans or len(ans) == 1 and (ans[0] == '+' or ans[0] == '-'):
            return 0
        ans = int(ans)
        intLimitMax = ((2 ** 31) -1)
        intLimitMin = -2 ** 31
        if ans > 0 and ans > intLimitMax:
            return intLimitMax
        elif ans < 0 and ans < intLimitMin:
            return intLimitMin
        return ans
            
        