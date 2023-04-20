class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [float('inf')] * N
        dp[N - 1] = 0
        for i in range(N - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < N:
                    dp[i] = min(dp[i], dp[i + j] + 1)
        return dp[0]