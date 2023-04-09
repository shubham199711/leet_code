class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        ans = 0
        prev = intervals[0][-1]
        print(prev)
        for i in range(1, len(intervals)):
            item = intervals[i]
            if item[0] < prev:
                ans += 1
                prev = min(prev, item[1])
            else:
                prev= max(prev, item[1])
        return ans
        