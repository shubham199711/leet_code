import math

class Solution:
    # with loops
    def isPowerOfTwoLopps(self, n: int) -> bool:
        if n == 1:
            return True
        while n > 2:
            if n % 2 == 1:
                return False
            n //= 2
        return n == 2
        
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & n-1)
        