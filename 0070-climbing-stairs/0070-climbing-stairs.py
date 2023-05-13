class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ans = [0] * n
        ans[0] = 1
        ans[1] = 2
        for i in range(2, n):
            ans[i] += ans[i - 1] + ans[i - 2]
        return ans[-1]
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)