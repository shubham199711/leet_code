class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0, 1]
        even = 1
        odd = 1
        for i in range(n - 1):
            if i % 2 == 0:
                dp.append(dp[even])
                even += 1
            else:
                dp.append(dp[odd] + dp[odd + 1])
                odd += 1
        return max(dp)
        