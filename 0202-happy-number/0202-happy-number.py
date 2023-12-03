class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) * int(x) for x in str(n)])
            if n == 1:
                return True
        return False
            
