class Solution:
    def maxArea(self, height: List[int]) -> int:
        _max = 0
        left, right = 0, len(height) - 1
        # 1 ,8
        while left < right:
            _max = max(_max, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return _max
        