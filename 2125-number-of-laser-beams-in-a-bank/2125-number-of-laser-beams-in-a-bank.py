class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        _ans = 0
        prevCount = 0
        for s in bank:
            count = s.count('1')
            if count:
                if prevCount == 0:
                    prevCount = count
                else:
                    _ans += (prevCount * count)
                    prevCount = count
        return _ans
        