class Solution:
    def merge(self, intervals):
        _ans = []
        for i in sorted(intervals, key = lambda x: x[0]):
            if _ans and i[0] <= _ans[-1][-1]:
                _ans[-1][-1] = max(_ans[-1][-1], i[1])
            else:
                _ans += [i]
        return _ans
        