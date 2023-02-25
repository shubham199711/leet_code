class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        _set = set([])
        _setOfAll = set([])
        for i , j in edges:
            _set.add(j)
            _setOfAll.add(i)
            _setOfAll.add(j)
        return _setOfAll - _set
        