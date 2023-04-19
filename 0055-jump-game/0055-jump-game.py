class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i):
            if i == len(nums) - 1:
                return True
            if i + nums[i] >= len(nums) - 1:
                return True
            for j in range(1, nums[i] + 1):
                j = j + i
                if j > len(nums) - 1:
                    break
                if dfs(j):
                    return True
            return False
        return dfs(0)
        