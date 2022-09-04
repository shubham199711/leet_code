class Solution:
    def coinChange_dp(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for money in range(1, amount + 1):
            for coin in coins:
                if money - coin >= 0:
                    dp[money] = min(dp[money], dp[money - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1