class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        _ans, prevCount = 0, 0
        for s in bank:
            count = s.count('1')
            if count:
                if prevCount != 0:
                    _ans += (prevCount * count)
                prevCount = count
        return _ans
        