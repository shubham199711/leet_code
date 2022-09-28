from math import factorial

class Solution:
    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j -1] + dp[j]
        return dp[-1] if m and n else 0
    
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n -2) // factorial(m -1) // factorial(n -1)