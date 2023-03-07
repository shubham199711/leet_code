class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # _ans = []
        # for item in sorted(intervals, key = lambda x: x[0]):
        #     if _ans and item[0] <= _ans[-1][-1]:
        #         _ans[-1][-1] = max(_ans[-1][-1], item[1])
        #     else:
        #         _ans += [item]
        # return _ans
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key = lambda x: x[0])
        prev = intervals[0]
        ans = []
        for item in intervals:
            if item[0] <= prev[1]:
                prev[1] = max(prev[1], item[1])
            else:
                ans.append(prev)
                prev = item
        ans.append(prev)
        return ans
        