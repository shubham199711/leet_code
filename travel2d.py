def nextPossiblePlay(x, y):
    yield [x+1, y]
    yield [x, y+1]


def isInValidPlay(_list, x, y):
    if x < 0 or y < 0:
        return True
    if y >= len(_list[0]) or x >= len(_list):
        return True
    return False


def _travelGrid(_list, end, x, y, count):
    if isInValidPlay(_list,  x, y) == True:
        return float('inf')
    if _list[x][y] == end:
        return count
    return min([_travelGrid(_list, end, item[0], item[1], count + 1) for item in nextPossiblePlay(x, y)])


def travelGridMain(_list, end):
    return _travelGrid(_list,  end, 0, 0, 0)


if __name__ == "__main__":
    _list = [[0, 0, 0], [0, 0, 1]]
    print(travelGridMain(_list, 1))
