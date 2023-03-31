class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org_val = image[sr][sc]
        if org_val == color:
            return image
        def bfs():
            stack = [(sr, sc)]
            while stack:
                i, j  = stack.pop(0)
                for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    _i = (i + ii)
                    _j = (j + jj)
                    if 0 <= _i < len(image) and 0 <= _j < len(image[0]):
                        if image[_i][_j] == org_val:
                            stack.append((_i, _j))
                image[i][j] = color
        bfs()
        return image
        