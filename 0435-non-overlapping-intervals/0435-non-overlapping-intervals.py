class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        ans = 0
        prev = intervals[0][-1]
        for i in range(1, len(intervals)):
            item = intervals[i]
            if item[0] < prev:
                ans += 1
                prev = min(prev, item[1]) # keep the one with minimum end values
            else:
                prev= max(prev, item[1]) # keep going with max end value
        return ans
        