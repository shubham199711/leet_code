class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _ans = ''
        for char in strs[0]:
            isStartWith = True
            _item  = _ans + char
            for item in strs:
                if not item.startswith(_item):
                    return _ans
            if isStartWith:
                _ans += char
        return _ans
                
                
        