class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        m = {}
        for item in arr:
            sortedItem = ''.join(sorted(item))
            if m.get(sortedItem) is not None:
                temp = m[sortedItem]
                temp.append(item)
                m[sortedItem] = temp
            else:
                m[sortedItem] = [item]
        _ans = []
        for key in m:
            _ans.append(m[key])
        return _ans