import re
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        _ansForS = []
        _ansForT = []
        for item in s:
            if item == '#':
                if len(_ansForS):
                    _ansForS.pop()
                    # _ansForS = _ansForS[:-1]
            else:
                _ansForS.append(item)
        for item in t:
            if item == '#':
                if len(_ansForT):
                    _ansForT.pop()
                    # _ansForT = _ansForT[:-1]
            else:
                _ansForT.append(item)
        return _ansForS == _ansForT
        