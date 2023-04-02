class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        m = len(heights)
        ans = [0] * m
        for i in range(m - 1, -1, -1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
                ans[i] += 1
            ans[i] += 1 if stack else 0
            stack.append(heights[i])
        return ans