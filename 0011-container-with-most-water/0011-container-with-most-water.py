class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            max_height_on_curent_level = min(height[left], height[right])
            # (right - left) gives width
            # max_height_on_curent_level gives min height
            # so area = width * height
            ans = max(ans, (right - left) * max_height_on_curent_level)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
            
        