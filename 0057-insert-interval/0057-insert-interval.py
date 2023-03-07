class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def findIndex():
            left, right = 0, len(intervals) - 1
            while left <= right:
                _mid = (left + right) // 2
                if intervals[_mid][0] < newInterval[0]:
                    left = _mid + 1
                else:
                    right = _mid - 1
            return left
        _index = findIndex()
        intervals.insert(_index, newInterval)
        prev = intervals[0]
        ans = []
        for item in intervals:
            if prev[1] >= item[0]:
                prev[1] = max(prev[1], item[1])
            else:
                ans.append(prev)
                prev = item
        ans.append(prev)
        return ans
                
        