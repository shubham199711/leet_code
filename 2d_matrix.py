
def findNode(data):
    if(data[0][0] == 2):
        return 0
    r, c = len(data[0]), len(data)
    visited = [[False for _ in range(r)] for _ in range(c)]
    def isValid(i,j):
        if i < 0 or j < 0 or i >= r or j >= c or data[i][j] == 0 or visited[i][j] == True:
            return False
        return True
    queue = [[0, 0]]
    ans = 0
    while len(queue) > 0:
        i, j = queue.pop(0)
        if isValid(i,j):
            visited[i][j] = True
            if data[i][j] == 2:
                print('Path length found to be: ', ans)
                return
            queue.append([i + 1,j])
            queue.append([i - 1,j])
            queue.append([i, j + 1])
            queue.append([i, j - 1])
            ans += 1
    print('Path not found')
    return

data = [[1,1,1],[0,1,0],[2,1,0]]
findNode(data)