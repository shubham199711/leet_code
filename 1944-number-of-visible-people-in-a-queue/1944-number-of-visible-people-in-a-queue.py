class Solution:
    def canSeePersonsCount2(self, heights: List[int]) -> List[int]:
        m = len(heights)
        ans = []
        for i in range(m):
            right = i + 1
            count = 0
            _max = float('-inf')
            while right < m:
                if heights[right] <= heights[i]:
                    if heights[right] >_max:
                        _max = heights[right]
                        right += 1
                        count += 1
                    else:
                        right += 1
                else:
                    count += 1
                    break
            ans.append(count)
        return ans
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0 for _ in range(n)]
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
                res[i] += 1
            res[i] += 1 if stack else 0
            stack.append(heights[i])
        return res
        