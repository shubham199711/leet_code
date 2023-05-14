class Solution:
    def minCostClimbingStairsdp(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 2)
        for i in range(n - 1, -1 , -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @lru_cache(None)
        def backtrack(i):
            if i >= n:
                return 0
            return cost[i] + min(backtrack(i + 1), backtrack(i + 2))
        return min(backtrack(0), backtrack(1))
