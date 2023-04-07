class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key= lambda x: x[0])
        ans = []
        prev = intervals[0]
        for item in intervals:
            if item[0] <= prev[1]:
                prev[1] = max(prev[1], item[1])
            else:
                ans.append(prev)
                prev = item
        ans.append(prev)
        return ans
