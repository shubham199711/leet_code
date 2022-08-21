class Solution:
    # def spiralOrder(self, matrix):
    #     return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
    def spiralOrder(self, matrix):
        _ans = []
        while matrix:
            _ans.extend([*matrix.pop(0)])
            matrix = [*zip(*matrix)][::-1]
        return _ans