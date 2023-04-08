class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # matrix[::] = zip(*matrix[::-1])
        # return
        '''
        We have to rotate first by horizontal axis and then
        transpose matrix to rotate by 90
        '''
        for i in range(len(matrix) // 2):
            matrix[i], matrix[~i]  = matrix[~i], matrix[i]
        # transpose only the top right part is moved to bottom left part
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]