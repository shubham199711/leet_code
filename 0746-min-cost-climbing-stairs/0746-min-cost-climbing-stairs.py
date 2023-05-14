class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        for i in range(n - 3, -1 , -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        n = len(cost)
        @lru_cache(None)
        def backtrack(i):
            if i >= n:
                return 0
            return cost[i] + min(backtrack(i + 1), backtrack(i + 2))
        return min(backtrack(0), backtrack(1))
