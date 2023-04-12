class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        _sum, l, r, n, ans  = 0, 0, 0, len(nums), float('inf')
        while l < n:
            while r < n and _sum < target:
                _sum += nums[r]
                r += 1
            # print(f'{l =}, {r = }, {ans = }, {_sum = }') 
            if _sum >= target:
                ans = min(ans, r - l)
            _sum -= nums[l]
            l += 1
        return ans if ans != float('inf') else 0
            
            
            
            
        