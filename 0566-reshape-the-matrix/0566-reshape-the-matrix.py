class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        def getNextElement():
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    yield mat[i][j]
                    
        itte = getNextElement() # generator to get next element
        ans = []
        for i in range(r):
            ans.append([next(itte) for x in range(c)])
        return ans