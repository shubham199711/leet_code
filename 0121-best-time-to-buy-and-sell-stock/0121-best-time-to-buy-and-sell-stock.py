class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 1)
        _min = prices[0]
        for i in range(1, n + 1):
            _min = min(_min, prices[i - 1])
            dp[i] = max(prices[i - 1] - _min, dp[i - 1])
        return dp[-1]
