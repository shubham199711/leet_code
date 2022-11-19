class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            rst = int(str(x)[::-1]) 
        else:
            rst =  -1 * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0