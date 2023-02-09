class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []
        mapOfMoving = {
            'R': [0 , 1],
             'L': [0, -1],
             'U': [-1 , 0],
             'D': [1 , 0],
        }
        def travelGrid(index):
            count = 0
            row,col = startPos[0], startPos[1]
            for i in range(index, len(s)):
                cRow, cCol = mapOfMoving[s[i]]
                row += cRow
                col += cCol
                if row >= 0 and row < n and col >= 0 and col < n:
                    count += 1
                else:
                    break
            return count
        
        for i in range(len(s)):
            ans.append(travelGrid(i))
        return ans
        