class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        memo = {}
        def memo_square(x):
            if memo.get(x) is not None:
                return memo[x]
            memo[x] = x * x
            return memo[x]
        while n not in seen:
            seen.add(n)
            n = sum([memo_square(int(x)) for x in str(n)])
            if n == 1:
                return True
        return False
            
