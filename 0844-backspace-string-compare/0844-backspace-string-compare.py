import re
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        _ansForS = []
        _ansForT = []
        for item in s:
            if item == '#':
                if len(_ansForS):
                    _ansForS.pop()
            else:
                _ansForS.append(item)
        for item in t:
            if item == '#':
                if len(_ansForT):
                    _ansForT.pop()
            else:
                _ansForT.append(item)
        return _ansForS == _ansForT
        