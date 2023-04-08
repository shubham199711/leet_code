class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[::] = zip(*matrix[::-1])
        return
        '''
        We have to rotate first by horizontal axis and then
        transpose matrix to rotate by 90
        '''
        # rotate
        # l = 0
        # r = len(matrix) -1
        # while l < r:
            # matrix[l], matrix[r] = matrix[r], matrix[l]
            # l += 1
            # r -= 1
        
        for i in range(len(matrix) // 2):
            _len = -1 -i
            matrix[i], matrix[_len]  = matrix[_len], matrix[i]
        # transpose 
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]