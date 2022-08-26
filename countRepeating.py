def countRep(_str):
    countDict = {}
    for char in _str:
        if countDict.get(char) is not None:
            countDict[char] += 1
        else:
           countDict[char] = 1 
    for char in _str:
        if countDict[char] == 1:
            return char
    return -1

print(countRep('thisisit'))