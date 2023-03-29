class Solution:
    def maxSatisfaction(self, nums: List[int]) -> int:
        nums, n = sorted(nums), len(nums)
        cur, s, ans = 0, 0, 0  # current_result, prefix_sum, final_answer 
        for i in range(n-1, -1, -1):
            s += nums[i] 
            cur += s
            ans = max(cur, ans)
        return ans
