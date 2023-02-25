import bisect

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        data = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                key = f'{i - j}'
                item = mat[i][j]
                if data.get(key) is not None:
                    bisect.insort(data[key], item)
                else:
                    data[key] = [item]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                key = f'{i - j}'
                item = data[key].pop(0)
                mat[i][j] = item
        return mat
        