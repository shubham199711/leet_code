class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        m = {}
        for item in arr:
            sortedItem = ''.join(sorted(item))
            if m.get(sortedItem) is not None:
                m[sortedItem].append(item)
            else:
                m[sortedItem] = [item]
        return [m[key] for key in m.keys()] 